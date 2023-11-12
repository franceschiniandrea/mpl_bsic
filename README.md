# MPL BSIC Package

## Installation

To install, run

```
pip install mpl_bsic
```

Then you can import the functions from the module, for example

The package supports all python versions starting from 3.9

```
from mpl_bsic import apply_bsic_style
```

## Docs and TLDR

Read the docs on [this link](https://mpl-bsic.readthedocs.io/).
All the functions are explained extensively and you can find example code/plots.

A brief overview of the functions of the module:

* `apply_bsic_style`: applies the BSIC styles to a plot (font families, font sizes).
* `apply_bsic_logo`: applies the BSIC logo to the plot. You can specify the size, location and logo type.
* `check_figsize`: checks the figsize of your plot, to make sure it will be rendered correctly in MS Word.
    To learn more about this, look at the documentation
* `format_timeseries_axis`: formats the x axis of a timeseries plot.
    You can specify the time unit (yearly, monthly, daily), the frequency (e.g. a tick every 3M), and the format (e.g. MM/YYYY or MMM YYYY)
* `preprocess_dataframe`: preprocesses a dataframe, by setting the index to the date (and converting to datetime)
    and transforming all the columns to lowercase for easier use in the project
* `plot_trade`: this function is WIP

## If the matplotlib fonts do not work

Check the full guide on the documentation. Anyway, you need to install
Garamond and Gill Sans MT and clear your matplotlib cache.

## Coming Next / TODOs (if you have any ideas be sure to tell me)

1) plot trade (as bloomberg with last price and stuff)