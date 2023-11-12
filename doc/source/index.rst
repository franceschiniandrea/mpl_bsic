.. af_utils documentation master file, created by
   sphinx-quickstart on Mon Nov  6 10:45:45 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Docs for mpl_bsic
====================================

``mpl_bsic`` helps you style matplotlib plots in BSIC style.

Installation
------------

The package supports Python versions from 3.9 onwards. It can be installed by using pip:

.. code-block:: python

   pip install mpl-bsic


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

Functions
---------

.. autosummary::
   :toctree: _functions

   mpl_bsic.apply_bsic_style
   mpl_bsic.check_figsize
   mpl_bsic.format_timeseries_axis
   mpl_bsic.preprocess_dataframe

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`