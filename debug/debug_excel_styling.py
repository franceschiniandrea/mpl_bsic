import debugconf  # noqa: F401
import numpy as np
import pandas as pd

from mpl_bsic import write_df_to_excel

# Create example dataframe with random data
data = {
    "A": np.random.randint(0, 100, 5),
    "B": np.random.randint(0, 100, 5),
    "C": np.random.randint(0, 100, 5),
}
df = pd.DataFrame(data, index="a b c d e".split())
df2 = df.copy()

offset = (2, 1)

write_df_to_excel(
    [df, df2],
    "debug/data/test.xlsx",
    ["title 1", "title 2"],
    "output_sheet",
    offset=offset,
)
# style_table.format_excel_file("test.xlsx", "output_sheet", "test title", "test_output")
