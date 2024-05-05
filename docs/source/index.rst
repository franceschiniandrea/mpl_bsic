.. af_utils documentation master file, created by
   sphinx-quickstart on Mon Nov  6 10:45:45 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Docs for mpl_bsic - Version |version| 
===================================================

``mpl_bsic`` helps you style matplotlib plots in BSIC style.

Setting up the Fonts (Optional)
-------------------------------

BSIC uses Gill Sans MT for Headings, and Garamond for text.
This library will temporarily install the fonts on your matplotlib
instance if you don't have them on your computer, but if you want
to install them, here's a quick explanation.

As of now, the process has only been tested on MacOS.
If it doesn't work on Windows, shoot me a message.

1) Download and install the fonts
    a) Download the fonts from the ``fonts`` folder in the main repository.
    b) Install the fonts (double click on the font files and click on "Install Font").
2) Clear your matplotlib cache.
    a) Go on ``your pc > users > [your-user] > .matplotlib``
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
(and :func:`apply_bsic_logo() <mpl_bsic.apply_bsic_logo>`) on the plot you want to style.

Be sure to read the docs for :func:`apply_bsic_style() <mpl_bsic.apply_bsic_style>` and
:func:`apply_bsic_logo() <mpl_bsic.apply_bsic_logo>` thoroughly to see how to use them correctly.

.. code:: python

    from mpl_bsic import apply_bsic_style

    fig, ax = plt.subplots(1,1)
    apply_bsic_style(fig, ax)
    ax.set_title('your title')

    ... # plot your data and apply the style
    # fig.tight_layout() # DO NOT call this before exporting

    # notice the arguments specified
    fig.savefig("your_filename.svg", dpi=1200, bbox_inches="tight")


.. rubric:: Exporting the plot

When exporting, we need to make sure that the figure is
not resized automatically by matplotlib and that
the font sizes stay consistent.
To do that, you **must not** call ``fig.tight_layout()`` before exporting. 
Additionally, you **must** export the figure with ``bbox_inches='tight'``
to make sure that no parts of the plot are cropped out.

My recommendation is to export in ``svg`` format, so that the quality of 
the image stays constant even when resizing (which, by the way, you should ideally
not do).

To export the figure, **use the provided function** ``mpl_bsic.export_figure``, 
which takes care of applying the styles and the correct parameters to the
``.savefig()`` function provided in vanilla Matplotlib.

.. code:: python

    from mpl_bsic import export_figure
    
    fig, ax = plt.subplots(1,1)

    ... # plot your data and apply the style
    # DO NOT call fig.tight_layout() this before exporting

    export_figure(fig, 'export_path') # specify the export path without the extension


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
   mpl_bsic.apply_bsic_logo
   mpl_bsic.add_title_subtitle
   mpl_bsic.plot_trade 
   mpl_bsic.export_figure
   mpl_bsic.check_figsize
   mpl_bsic.format_timeseries_axis
   mpl_bsic.preprocess_dataframe
   mpl_bsic.df_to_excel
   mpl_bsic.style_excel_file

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`