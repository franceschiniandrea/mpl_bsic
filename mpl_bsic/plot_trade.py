from typing import Literal

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.axes import Axes

from .apply_bsic_logo import apply_bsic_logo
from .apply_bsic_style import apply_bsic_style
from .format_timeseries_axis import format_timeseries_axis


def _plot_xline(ax: Axes, y: float, trade_start: str, color: str):
    bbox_props = dict(boxstyle="round", fc="w", ec="k", lw=1)
    y_min, y_max = ax.get_ylim()

    ax.hlines(
        y=[y],
        xmin=trade_start,
        xmax=ax.get_xbound()[1],
        color=color,
        linewidth=1,
        linestyle="-",
        alpha=0.75,
    )
    ax.annotate(
        str(round(y, 2)),
        xycoords="axes fraction",
        xy=(1.02, (y - y_min) / (y_max - y_min)),
        size=8,
        bbox=bbox_props,
        verticalalignment="center",
    )


def _plot_last_price(ax: Axes, data: pd.Series):
    """Plots the last price of the series on the right side of the plot."""
    # plot last price
    last_price = float(data.iloc[-1])
    y_min, y_max = ax.get_ylim()

    bbox_props = dict(boxstyle="round", fc="w", ec="k", lw=0.75)
    ax.annotate(
        str(int(last_price)),
        xycoords="axes fraction",
        xy=(1.02, (last_price - y_min) / (y_max - y_min)),
        size=8,
        bbox=bbox_props,
        verticalalignment="center",
    )


def _get_dates(
    underlying: pd.Series, pnl: pd.Series, months_offset: int
) -> tuple[pd.DatetimeIndex, pd.Timestamp]:
    """Gets the dates for the trade."""
    if not isinstance(underlying.index, pd.DatetimeIndex):
        raise Exception("Index of underlying must be a DatetimeIndex")

    if not isinstance(pnl.index, pd.DatetimeIndex):
        raise Exception("Index of PnL must be a DatetimeIndex")

    dates = underlying.index

    end_date = dates[-1]
    start_date = end_date - pd.DateOffset(months=months_offset)
    entry_date = pnl.dropna().index[0]

    dates = dates[(dates >= start_date) & (dates <= end_date)]

    if not isinstance(entry_date, pd.Timestamp):
        raise Exception("There was an issue pulling the entry date for the trade.")

    return dates, entry_date


def _plot_entry_point(
    ax: Axes,
    entry_date: pd.Timestamp,
    underlying: pd.Series,
    marker_location: Literal["top", "bottom"],
    marker_size: int,
):
    """Plots the entry point of the trade."""

    offset = 0.075 if marker_location == "top" else -0.075
    marker = "v" if marker_location == "top" else "^"

    price_at_entry = underlying.loc[entry_date]
    marker_loc = price_at_entry * (1 + offset)

    ax.scatter(
        [entry_date.strftime("%Y-%m-%d")],
        [marker_loc],
        color="g",
        marker=marker,
        s=marker_size,
    )


def _preprocess_data(
    underlying: pd.Series, pnl: pd.Series, dates: pd.DatetimeIndex, pnl_type: str
):
    """Preprocesses the data."""
    underlying = underlying.copy().loc[dates]
    pnl = pnl.copy()

    if pnl_type == "nominal":
        pass
    elif pnl_type == "cumulative":
        pnl = pnl.cumsum()
    else:
        raise Exception(
            'pnl type is not supported. Supported are "nominal" and "cumulative".'
        )

    pnl.fillna(0, inplace=True)

    return underlying, pnl


def plot_trade(
    underlying: pd.Series,
    pnl: pd.Series,
    pnl_type: Literal["nominal", "cumulative"],
    title: str,
    underlying_name: str,
    months_offset: int = 3,
    entry_point_marker_loc: Literal["top", "bottom"] = "top",
    entry_point_marker_size: int = 10,
    date_ticks_unit: Literal["Y", "M", "W", "D"] = "W",
    date_ticks_freq: int = 1,
    date_ticks_format: str = "%b %d, %Y",
):
    """
    Plot a trade performance vs the underlying.

    Create a figure with two subplots. On the top, the PnL of the trade is plotted,
    while on the bottom the underlying is plotted.

    The function automatically applies BSIC Style and
    Logo through the respective functions.

    Parameters
    ----------
    underlying : pd.Series
        Pandas series of the underlying's prices.
    pnl : pd.Series
        Pandas series of the pnl of the trade. This must be in nominal terms
        or in percentage terms,
        if you want to plot the percentages. You can also plot the cumulative PnL,
        the function will calculate it for you.
    pnl_type : Literal['Nominal', 'Cumulative']
        The type of PnL you want to plot. Can be "Nominal" or "Cumulative".
        If "nominal", the function will plot the PnL as is.
        If "cumulative", the function will plot the cumulative PnL by doing
        `.cumsum()` on the PnL series.
    title : str
        The title of the trade. This will be set as the suptitle of the figure.
    underlying_name : str
        The name of the underlying that will be plotted on the bottom subplot,
        for example "Swap Spread", "EURUSD", etc.
    months_offset : int, optional
        The months offset that will be used to calculate the first date plotted,
        by default 3. Since it is a trade,
        it is recommended to set a short offset (like 3 as the default),
        so that you can easily see the path of the underlying
        after you entered the trade.
    entry_point_marker_loc : Literal['top', 'bottom'], optional
        The location of the marker for the entry point, by default "top".
        Whether it is better to use "top" or "bottom" depends
        on the type of trade you are plotting and the shape of the plot.
        Choose so that the marker is clearly visible and
        does not overlap with the underlying's plot.
    entry_point_marker_size : int, optional
        The size of the entry point market, by default 10. Choosing this size will
        depend on the final size of the plot.
        Choose so that the marker is clearly visible and does not overlap with the
        underlying's plot.
    date_ticks_unit : Literal['Y', 'M', 'W', 'D'], optional
        The unit used to segment the datetime index (which is displayed
        on the bottom axis), by default "W". Since you
        are probably going to plot a short timespan, it is recommended to use either
        "W" (weeks) or "D" (days). There should
        be no reason to use "Y" (years), and you should really question the timeframe
        you are using if you are choosing "M".
    date_ticks_freq : int, optional
        The frequency for the ticks in the unit specified, by default 1. For example,
        if you chose "W" as the unit, and 1 as the
        frequency, there will be 1 tick every week.
        Choose so that the axis is not cluttered.
    date_ticks_format : str, optional
        The format used for the date ticks, by default "%b %d, %Y". I recommend
        using the default, but you can change it to whatever
        you find more suitable

    Returns
    -------
    tuple[matplotlib.figure.Figure, matplotlib.axes.Axes]
        A tuple containing the figure and the tuple of two axis just created.
        You can later use this to save the fig for export, do `fig.show()`,
        or further customize the plot.

    See Also
    --------
    mpl_bsic.apply_bsic_style :
        Apply the BSIC style to a plot.
    mpl_bsic.apply_bsic_logo :
        Apply the BSIC logo to a plot.
    mpl_bsic.check_figsize :
        Check if the figsize is valid.

    Examples
    --------
    Examples will come soon.


    """
    dates, entry_date = _get_dates(underlying, pnl, months_offset)

    underlying, pnl = _preprocess_data(underlying, pnl, dates, pnl_type)

    # creates plots
    fig, axs = plt.subplots(
        2, 1, sharex=True, gridspec_kw={"hspace": 0.1, "height_ratios": [1.25, 2]}
    )
    pnl_ax, underlying_ax = axs
    pnl_ax: Axes
    underlying_ax: Axes

    # sets title and applies style
    if title is not None:
        fig.suptitle(title)

    apply_bsic_style(fig, axs)

    # plot the data
    underlying_ax.plot(underlying.index, underlying)
    pnl_ax.plot(pnl.index, pnl)
    pnl_ax.axhline(0, color="black", linewidth=1, alpha=0.75)

    # set labels
    underlying_ax.set_ylabel(underlying_name)
    pnl_ax.set_ylabel("PnL")

    # formats dates
    format_timeseries_axis(
        underlying_ax, date_ticks_unit, date_ticks_freq, date_ticks_format
    )

    # apply logo
    apply_bsic_logo(fig, pnl_ax, location="top left")

    # plot last price
    _plot_last_price(underlying_ax, underlying)
    _plot_last_price(pnl_ax, pnl)

    # plot entry point
    _plot_entry_point(
        underlying_ax,
        entry_date,
        underlying,
        entry_point_marker_loc,
        entry_point_marker_size,
    )

    # plot areas of profit and loss
    pnl_ax.fill_between(
        pnl.index,
        0,
        pnl,
        where=(pnl >= 0),  # type: ignore
        color="g",
        alpha=0.3,
        interpolate=True,
        lw=0,
    )
    pnl_ax.fill_between(
        pnl.index,
        0,
        pnl,
        where=(pnl < 0),  # type: ignore
        color="r",
        alpha=0.3,
        interpolate=True,
    )

    # # plot stop loss and take profit
    # trade_start = pnl[pnl["pnl"] > 0].index[-1]
    # print(trade_start, pnl, pnl[pnl > 0])
    # if stop_loss is not None:
    #     _plot_xline(underlying_ax, stop_loss, trade_start=trade_start, color="r")
    # if take_profit is not None:
    #     _plot_xline(underlying_ax, take_profit, trade_start=trade_start, color="g")

    # underlying_ax.set_xlim(xlims)

    return fig, axs
