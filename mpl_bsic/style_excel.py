from typing import Optional, Union

import pandas as pd
import xlsxwriter

TITLE_FMT = {
    "bold": True,
    "italic": True,
    "align": "center",
    "valign": "center",
    "font_size": 11,
    "font_name": "Gill Sans MT",
}

HEADER_FMT = {
    "font_name": "Gill Sans MT",
    "font_size": 11,
    "italic": True,
    "bold": True,
    "text_wrap": True,
    "valign": "top",
    "align": "center",
    "fg_color": "#38329A",
    "color": "white",
    "top": 1,
    "bottom": 1,
}

BASE_BODY_FMT = {
    "font_name": "Garamond",
    "font_size": 12,
    "text_wrap": True,
    "valign": "top",
    "align": "center",
}

INDEX_FMT = BASE_BODY_FMT | {
    "bold": True,
    "right": 1,
    "left": 1,
    "bottom": 1,
}


def _format_worksheet(
    wb,
    ws,
    df: pd.DataFrame,
    title: Optional[str],
    offset: tuple[int, int],
    write_sources: bool = True,
):
    # check that the workbook and worksheet are valid
    if not isinstance(wb, xlsxwriter.workbook.Workbook):
        raise Exception("Workbook is not an xlsxwriter workbook")

    if not isinstance(ws, xlsxwriter.workbook.Worksheet):
        raise Exception("Worksheet is not an xlsxwriter worksheet")

    title_offset = 0 if title is None else 1

    start_row, start_col = offset
    # +1 to end_row to account for the title
    end_row = df.shape[0] + start_row + title_offset
    end_col = df.shape[1] + start_col

    def _write_index(df: pd.DataFrame):
        def index_format(i):
            fmt = INDEX_FMT | {
                "top": 1 if i == start_row else 0,
                "bottom": 1 if i == end_row else 0,
            }

            return wb.add_format(fmt)

        for row_num, value in enumerate(df.index.values):
            # leave space for the title and headings
            row_index = start_row + row_num + 1 + title_offset
            ws.write(row_index, start_col, value, index_format(row_index))

    def _write_data(df: pd.DataFrame, sources: str):
        def header_format(i):
            fmt = HEADER_FMT | {
                "left": 1 if i == start_col else 0,
                "right": 1 if i == end_col else 0,
            }

            return wb.add_format(fmt)

        def text_format(i: int):
            fmt = BASE_BODY_FMT | {
                "bottom": 1,
                "right": 1 if i == end_col else 0,
            }

            return wb.add_format(fmt)

        # write headers and data
        header_row_index = start_row + title_offset  # leave space for the title
        for i, col_name in enumerate(df.columns):
            col_index = start_col + i + 1  # leave space for the index names

            # write headers
            ws.write(header_row_index, col_index, col_name, header_format(col_index))

            # write data
            data = df[col_name].values
            for j, item in enumerate(data):
                row_index = header_row_index + j + 1
                ws.write(row_index, col_index, item, text_format(col_index))

        # write index name
        ws.write(header_row_index, start_col, df.index.name, header_format(0))

        # write sources
        if write_sources:
            sources_row_idx = end_row + 2
            ws.merge_range(
                sources_row_idx,
                start_col,
                sources_row_idx,
                end_col,
                f"Source: {sources}",
                wb.add_format(BASE_BODY_FMT),
            )
            ws.set_row(sources_row_idx - 1, 5)

    # set the correct row height
    ws.set_default_row(15.5)

    if isinstance(title, str):
        title_format = wb.add_format(TITLE_FMT)
        ws.merge_range(start_row, start_col, start_row, end_col, title, title_format)

    _write_index(df)
    _write_data(df, "BSIC")

    ws.hide_gridlines(2)


def write_df_to_excel(
    df: Union[pd.DataFrame, list[pd.DataFrame]],
    path_to_excel: str,
    title: Optional[Union[str, list[str]]] = None,
    output_sheet: Optional[str] = "output",
    offset: tuple[int, int] = (1, 1),
):
    # create a new excel file with the formatted data from the dataframe
    wb = xlsxwriter.Workbook(path_to_excel)
    ws = wb.add_worksheet(output_sheet)

    if isinstance(df, list):
        if not isinstance(title, list):
            raise Exception(
                "If you provide a list of dataframes, you must provide a list of titles"
            )
        if not len(df) == len(title):
            raise Exception(
                "If you provide a list of dataframes, you must provide a list of titles of the same length"  # noqa: E501
            )

        ws_col0 = offset[0]

        ws_colend = ws_col0 + sum([_df.shape[1] for _df in df]) + len(df)
        row_source = offset[1] + max([_df.shape[0] for _df in df]) + 4

        for i, (_df, _title) in enumerate(zip(df, title)):
            new_start_col = offset[1] + i * _df.shape[0] + 1
            df_offset = (offset[0], new_start_col)
            _format_worksheet(wb, ws, _df, _title, df_offset, write_sources=False)

            ws.set_column(new_start_col - 1, new_start_col - 1, 3)

        ws.set_row(row_source - 1, 5)
        ws.merge_range(
            row_source,
            ws_col0,
            row_source,
            ws_colend,
            "Source: BSIC",
            wb.add_format(BASE_BODY_FMT),
        )

    else:
        if isinstance(title, list):
            raise Exception(
                "If you provide a single dataframe, you can only provide a single title"
            )

        _format_worksheet(wb, ws, df, title, offset)

    print("closing wb")
    wb.close()


def format_excel_file(
    path_to_excel: str,
    sheet_name: str,
    title: Optional[str],
    output_sheet: Optional[str] = "output",
    offset: tuple[int, int] = (1, 1),
):
    # format the already existing excel file
    df = pd.read_excel(path_to_excel, sheet_name=sheet_name, index_col=0)
    print(df)
    fmt_path = path_to_excel.replace(".xlsx", "_fmt.xlsx")
    wb = xlsxwriter.Workbook(fmt_path)
    ws = wb.add_worksheet(output_sheet)

    _format_worksheet(wb, ws, df, title, offset)

    wb.close()
