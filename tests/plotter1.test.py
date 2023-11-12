import pandas as pd
import test_setup  # noqa
from bsicplotter import BSICPlotter

plotter = BSICPlotter()

data = pd.read_csv("tests/data/usyieldsdata.csv")

print(data)
plotter.preprocess_dataframe(data)
print(data)
