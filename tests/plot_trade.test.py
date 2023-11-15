import pandas as pd
import test_setup  # noqa

from mpl_bsic import plot_trade, preprocess_dataframe

data = pd.read_excel("tests/data/trade.xlsx")
preprocess_dataframe(data)

fig, axs = plot_trade(
    data[["underlying"]],
    data[["pnl"]],
    title="Swap Spread Trade",
    stop_loss=300,
    take_profit=400,
)
