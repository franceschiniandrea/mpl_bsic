from typing import Literal, Optional

import matplotlib.dates as mdates
from matplotlib.axes import Axes


def format_timeseries_axis(
    ax: Axes,
    time_unit: Literal["Y", "M", "W", "D"],
    freq: int,
    fmt: Optional[str] = None,  # for backwards compatibility
):
    """Format the x-axis of a timeseries plot.

    It sets the major locator and formatter for the x-axis.
    Note that this function does not take as an input the figure,
    but just the matplotlib Axes instance.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Matplotlib Axes instance.
    time_unit : Literal['Y', 'M', 'W', 'D']
        Time unit to use.
        Can be "Y" for years, "M" for months, 'W' for weeks, or "D" for days.
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

    if time_unit == "Y":
        ax.xaxis.set_major_locator(mdates.YearLocator(freq))
    elif time_unit == "M":
        ax.xaxis.set_major_locator(mdates.MonthLocator(interval=freq))
    elif time_unit == "W":
        ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=freq))
    elif time_unit == "D":
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=freq))
    else:
        raise Exception("this time frequency is not supported.")

    date_format = fmt if fmt else "%b-%y"
    ax.xaxis.set_major_formatter(mdates.DateFormatter(date_format))
    ax.tick_params(axis="x", rotation=45)
