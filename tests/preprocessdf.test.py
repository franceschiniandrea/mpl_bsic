import pandas as pd
import test_setup  # noqa
from mpl_bsic import preprocess_dataframe

data = pd.read_csv("tests/data/usyieldsdata.csv")

print(data)
preprocess_dataframe(data)
print(data)
