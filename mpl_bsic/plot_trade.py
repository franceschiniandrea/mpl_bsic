from typing import Optional

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.axes import Axes

from mpl_bsic import apply_bsic_style


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


def plot_trade(
    underlying: pd.DataFrame,
    pnl: pd.DataFrame,
    title: Optional[str] = None,
    stop_loss: Optional[float] = None,
    take_profit: Optional[float] = None,
):
    """
    TODO Summary

    Parameters
    ----------
    underlying : pd.DataFrame
        _description_
    pnl : pd.DataFrame
        _description_
    """

    pnl = pnl.copy().reindex(underlying.index)
    pnl.fillna(0, inplace=True)

    fig, axs = plt.subplots(
        2, 1, sharex=True, gridspec_kw={"hspace": 0.1, "height_ratios": [1, 2]}
    )

    axs: list[Axes]

    pnl_ax, underlying_ax = axs
    if title is not None:
        pnl_ax.set_title(title)

    apply_bsic_style(fig, pnl_ax)
    apply_bsic_style(fig, underlying_ax)

    underlying_ax.plot(underlying.index, underlying)
    underlying_ax.set_ylabel("Underlying")
    pnl_ax.plot(pnl.index, pnl)
    # pnl_ax.set_xticks([])
    pnl_ax.set_ylabel("PnL")

    xlims = underlying_ax.get_xlim()

    # plot last price
    last_price = float(underlying.iloc[0])  # type: ignore
    y_min, y_max = underlying_ax.get_ylim()
    bbox_props = dict(boxstyle="round", fc="w", ec="k", lw=1)
    underlying_ax.annotate(
        str(int(last_price)),
        xycoords="axes fraction",
        xy=(1.02, (last_price - y_min) / (y_max - y_min)),
        size=8,
        bbox=bbox_props,
        verticalalignment="center",
    )

    # plot stop loss and take profit
    trade_start = pnl[pnl["pnl"] > 0].index[-1]
    print(trade_start, pnl, pnl[pnl > 0])
    if stop_loss is not None:
        _plot_xline(underlying_ax, stop_loss, trade_start=trade_start, color="r")
    if take_profit is not None:
        _plot_xline(underlying_ax, take_profit, trade_start=trade_start, color="g")

    underlying_ax.set_xlim(xlims)

    plt.show()
    return fig, axs
