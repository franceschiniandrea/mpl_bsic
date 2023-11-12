import pandas as pd
import matplotlib.pyplot as plt
import test_setup  # noqa
from bsicplotter import BSICPlotter

pltr = BSICPlotter()


data = pd.read_csv("tests/data/usyieldsdata.csv")
pltr.preprocess_dataframe(data)
data["2s10s"] = (data["us10y"] - data["us02y"]) * 100

options = {
    "title": "US 2s10s Differential (bps)",
    # 'constant_distance': False,
    "width": 8,
    "height": 3,
    "zero_line": False,
    "timeseries_ticks_unit": "M",
    "timeseries_ticks_frequency": 1,
    "legend": True,
    "legend_labels": ["US10Y", "US30Y"],
}

fig, ax = pltr.plot(data[["us10y", "us30y"]], **options)
plt.show()
