import pandas as pd
from mpl_bsic import apply_bsic_style
from matplotlib.axes import Axes
import matplotlib.pyplot as plt


def plot_trade(underlying: pd.DataFrame, pnl: pd.DataFrame):
    """
    TODO Summary

    Parameters
    ----------
    underlying : pd.DataFrame
        _description_
    pnl : pd.DataFrame
        _description_
    """
    fig, axs = plt.subplots(2, 1)
    title = "test title"

    axs: list[Axes]

    underlying_ax, pnl_ax = axs
    pnl_ax.set_title(title)
    apply_bsic_style(fig, pnl_ax)
    apply_bsic_style(fig, underlying_ax)

    underlying_ax.plot(underlying)
    pnl_ax.plot(pnl)
