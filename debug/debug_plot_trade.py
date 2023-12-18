import debugconf  # noqa
import matplotlib.pyplot as plt
import pandas as pd

from mpl_bsic import plot_trade

trade = pd.read_excel("tests/data/trade.xlsx", index_col=0)
trade.sort_index(inplace=True)

plot_trade(
    trade["Underlying"], trade["PnL"], "nominal", "Swap Spreads Trade", "Swap Spread"
)

plt.show()
