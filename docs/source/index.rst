.. af_utils documentation master file, created by
   sphinx-quickstart on Mon Nov  6 10:45:45 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Docs for mpl_bsic
====================================

``mpl_bsic`` helps you style matplotlib plots in BSIC style.

Setting up
----------

To make sure the plots are styled correctly, you must make sure that the fonts
are installed on your computer and that matplotlib can recognize them.
For now the process has been tested only on Macos.
If it doesn't work on Windows, shoot me a message.

1) Download and install the fonts
    a) Download the fonts from the ``fonts`` folder in the main repository.
    b) Install the fonts (double click on the font files and click on "Install Font").
2) Clear your matplotlib cache.
    a) Go on your pc > users > [your-user] > .matplotlib
    b) If you cannot see the .matplotlib folder,
        press ``cmd + shift + .`` to show hidden files.
    c) Delete the ``fontlist-vXXX.json`` file.

[IMPORTANT] Plotting for BSIC Articles
---------------------------------------------------------
This section will explain how to correctly create plots for BSIC articles.

.. rubric:: Choosing the figsize

Word documents have a maximum width of 7.32 inches.
Any image larger than that will be resized to fit the page.
If you end up resizing your image after exporting (or if Word does it for you),
*the font size of the Title of the plot won't match the font size
of the subsection titles in the article*.
Also, you won't have consistent font sizes
if you include more than 1 plot in the document.

To avoid this, you should **always** set the width of the figure to
**at most** 7.32 inches before exporting.
To get correct figsizes to use, and check that you set them correctly,
you can use :func:`check_figsize() <mpl_bsic.check_figsize>`.

.. rubric:: Plotting the data correctly

In your python file, you will call :func:`apply_bsic_style() <mpl_bsic.apply_bsic_style>`
on the plot you want to style.
To make sure that the title is rendered with the correct style
(it should be Gill Sans MT Bold & Italic, and a slightly larger
font size than the other text),
you must define it **before** calling :func:`apply_bsic_style() <mpl_bsic.apply_bsic_style>`,
or it won't be styled correctly.
Another option is to provide the function with the title as an argument.

Be sure to read the docs for :func:`apply_bsic_style() <mpl_bsic.apply_bsic_style>`
thoroughly to see how to use it correctly.

.. code:: python

    from mpl_bsic import apply_bsic_style
    fig, ax = plt.subplots(1,1)
    apply_bsic_style(fig, ax, title="YOUR TITLE HERE")

    ... # plot your data and apply the style
    # fig.tight_layout() # DO NOT call this before exporting

    fig.savefig("your_filename.svg", dpi=1200, bbox_inches="tight")


.. rubric:: Exporting the plot

When exporting, we need to make sure that the figure is
not resized automatically by matplotlib and that
the font sizes stay consistent.
To do that, you **must not** call ``fig.tight_layout()`` before exporting.

Additionally, you **must** export the figure with ``bbox_inches='tight'``
to make sure that no parts of the plot are cropped out.

My personal recommendation is to **export in svg** and **set dpi to 1200**,
so that the quality will be the best possible.

.. code:: python

    fig, ax = plt.subplots(1,1)

    ... # plot your data and apply the style
    # fig.tight_layout() # DO NOT call this before exporting

    fig.savefig("your_filename.svg", dpi=1200, bbox_inches="tight")


Specific Use Cases
------------------
.. rubric:: Plotting Yield Curves

When plotting yield curves, to make the x ticks the same distance,
regardless of time:

.. code:: python

    data.index = data.index.astype(str)

Functions
---------

.. autosummary::
   :toctree: _functions

   mpl_bsic.apply_bsic_style
   mpl_bsic.check_figsize
   mpl_bsic.format_timeseries_axis
   mpl_bsic.preprocess_dataframe
   mpl_bsic.apply_bsic_logo

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`