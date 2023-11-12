from typing import Literal
from matplotlib.axes import Axes
import matplotlib.dates as mdates


def format_timeseries_axis(
    ax: Axes, time_unit: Literal["Y", "M", "D"], freq: int, fmt: str | None
):
    """Format the x-axis of a timeseries plot.

    It sets the major locator and formatter for the x-axis.
    Note that this function does not take as an input the figure,
    but just the matplotlib Axes instance.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Matplotlib Axes instance.
    time_unit : Literal['Y', 'M', 'D']
        Time unit to use.
        Can be "Y" for years, "M" for months, or "D" for days.
    freq : int
        Time Frequency. For example, if time_unit is "M" and freq is 3,
        then the x-axis will have a tick every 3 months.
    fmt : str | None
        Date Format which will be fed to matplotlib.dates.DateFormatter.
        If None, the default format will be used (`%b-%y`).

    Raises
    ------
    Exception
        If the time frequency is not supported.

    See Also
    --------
    mpl_bsic.apply_BSIC_style :
        The function that applies the style to the plot.

    Examples
    --------
    Examples will come soon.
    """

    match time_unit:
        case "Y":
            ax.xaxis.set_major_locator(mdates.YearLocator(freq))
        case "M":
            ax.xaxis.set_major_locator(mdates.MonthLocator(interval=freq))
        case "D":
            ax.xaxis.set_major_locator(mdates.DayLocator(freq))
        case _:
            raise Exception("this time frequency is not supported.")

    date_format = fmt if fmt else "%b-%y"
    ax.xaxis.set_major_formatter(mdates.DateFormatter(date_format))
    ax.tick_params(axis="x", rotation=45)
