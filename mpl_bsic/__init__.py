"""``mpl_bsic`` helps you style matplotlib plots in BSIC style.

Setting up
----------

To make sure the plots are styled correctly, you must make sure that the fonts
are installed on your computer and that matplotlib can recognize them.
For now the process has been tested only on Macos.
If it doesn't work on Windows, shoot me a message.

1) Download the fonts from the `fonts` folder in this repository.
2) Install the fonts
    (double click on the font files and click on "Install Font").
3) Clear your matplotlib cache.
    a) Go on your pc > users > [your-user] > .matplotlib
    b) If you cannot see the .matplotlib folder,
        press ``cmd + shift + .`` to show hidden files.
    c) Delete the ``fontlist-vXXX.json`` file.

Guidelines
------------------
.. rubric:: Plotting Yield Curves

When plotting yield curves, to make the x ticks the same distance,
regardless of time:

.. code:: python

    data.index = data.index.astype(str)

.. rubric:: Saving the figure

When saving the figure, you should use ``bbox_inches='tight'``
to make sure the figure is not cropped.

.. code:: python

    fig, ax = plt.subplots(1,1)

    ... # plot your data and apply the style

    fig.savefig("your_filename.svg", dpi=1200, bbox_inches="tight")

Module Components
-----------------
"""

from .apply_bsic_style import apply_bsic_style  # noqa
from .check_figsize import check_figsize  # noqa
from .plot_trade import plot_trade  # noqa
from .format_timeseries_axis import format_timeseries_axis  # noqa
from .preprocess_dataframe import preprocess_dataframe  # noqa
from .apply_bsic_logo import apply_bsic_logo  # noqa
