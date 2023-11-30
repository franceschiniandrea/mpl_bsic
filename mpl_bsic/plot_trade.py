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
    TODO Summary
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
