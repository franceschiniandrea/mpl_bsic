import pandas as pd


def preprocess_dataframe(df: pd.DataFrame):
    """Handle and preprocess the DataFrame before plotting.

    Handle and preprocess the DataFrame before plotting.
    It sets all the columns to lowercase and
    sets the index as the dates (converting to datetime).

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to preprocess.

    See Also
    --------
    mpl_bsic.apply_BSIC_style :
        The function that applies the style to the plot.

    Examples
    --------
    This is the examples section. WIP.
    """

    df.columns = [col.lower() for col in df.columns]

    if "date" in df.columns:
        df.set_index("date", inplace=True, drop=True)
        df.index = pd.to_datetime(df.index)
