from cycler import cycler
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from typing import Optional

DEFAULT_TITLE_STYLE = {
    "fontname": "Gill Sans MT",
    "color": "black",
    "fontweight": "bold",
    "fontstyle": "italic",
    "fontsize": 12,
}
"""Default Title Style. Used in ``apply_bsic_style``.

Details:

* ``fontname``: ``Gill Sans MT``
* ``color``: ``black``
* ``fontweight``: ``bold``
* ``fontstyle``: ``italic``
* ``fontsize``: ``12``

See Also
--------
apply_bsic_style : The function that applies the style to the plot.
mpl_bsic.DEFAULT_COLOR_CYCLE :
    The default color cycler that gets applied to the plot.
mpl_bsic.DEFAULT_FONT_SIZE :
    The default font size that gets applied to the plot.

Examples
--------
This is the examples section. WIP.
"""

DEFAULT_COLOR_CYCLE = cycler(
    color=["#38329A", "#8EC6FF", "#601E66", "#2F2984", "#0E0B54"]
)
"""Default Color Style.

Cycle:

* ``#38329A``
* ``#8EC6FF``
* ``#601E66``
* ``#2F2984``
* ``#0E0B54``

See Also
--------
mpl_bsic.apply_bsic_style : The function that applies the style to the plot.
mpl_bsic.DEFAULT_TITLE_STYLE :
    The default title style that gets applied to the plot.
mpl_bsic.DEFAULT_FONT_SIZE :
    The default font size that gets applied to the plot.

Examples
--------
This is the examples section. WIP.
"""

DEFAULT_FONT_SIZE = 10
"""Default Font Size for the plot (text, labels, ticks).

The default font size used for the plots is 10.

See Also
--------
mpl_bsic.apply_bsic_style : The function that applies the style to the plot.
mpl_bsic.DEFAULT_TITLE_STYLE :
    The default title style that gets applied to the plot.
mpl_bsic.DEFAULT_COLOR_CYCLE :
    The default color cycler that gets applied to the plot.

Examples
--------
This is the examples section. WIP.
"""

BSIC_FONT_FAMILY = "Garamond"
"""Default Font Family for the plot (text, labels, ticks).

The default font family used for the plots is ``Garamond``.

See Also
--------
mpl_bsic.apply_bsic_style : The function that applies the style to the plot.
mpl_bsic.DEFAULT_TITLE_STYLE :
    The default title style that gets applied to the plot.
mpl_bsic.DEFAULT_FONT_SIZE :
    The default font size that gets applied to the plot.

Examples
--------
This is the examples section. WIP.
"""


def apply_bsic_style(fig: Figure, ax: Axes, title: Optional[str] = None):
    r"""Apply the BSIC Style to an existing matplotlib plot.

    Apply the BSIC Style to the plot. First, it sets the font family and size
    for the overall plot and the color cycle to use.
    Then, if the plot has a title, then it applies the default title style.

    Should be called *before* plotting, to make sure
    the right color cycle gets applied.

    Warning: if you want to specify and set a title to the plot,
    you can either set it before or give it to the function.
    Otherwise, the correct style won't be applied.
    This is forced by matplotlib
    and must be done to make sure the fuction works.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Matplotlib Figure instance.
    ax : matplotlib.axes.Axes
        Matplotlib Axes instance.
    title : str | None
        Title of the plot.
        If None, it will try to get the title from the Axes instance.

    See Also
    --------
    mpl_bsic.DEFAULT_TITLE_STYLE :
        The default title style that gets applied to the plot.
    mpl_bsic.DEFAULT_COLOR_CYCLE :
        The default color cycler that gets applied to the plot.
    mpl_bsic.DEFAULT_FONT_SIZE :
        The default font size that gets applied to the plot.

    Examples
    --------
    .. plot::

        from mpl_bsic import apply_bsic_style

        x = np.linspace(0, 5, 100)
        y = np.sin(x)

        fig, ax = plt.subplots(1, 1)
        # apply right after creating the Figure and Axes instances
        apply_bsic_style(fig, ax, 'Sin(x)')

        ax.plot(x,y)

    .. plot::

        from mpl_bsic import apply_bsic_style

        x = np.linspace(0, 5, 100)
        y = np.cos(x)

        fig, ax = plt.subplots(1, 1)
        # ax.set_title('Cos(x)') # set the title before applying the style
        # the function will re-set the title with the correct style
        apply_bsic_style(fig, ax)

        ax.plot(x,y)
    """
    plt.rcParams["font.sans-serif"] = BSIC_FONT_FAMILY
    plt.rcParams["font.size"] = DEFAULT_FONT_SIZE
    plt.rcParams["axes.prop_cycle"] = DEFAULT_COLOR_CYCLE
    ax.set_prop_cycle(DEFAULT_COLOR_CYCLE)

    if title is None:
        title = ax.get_title()
        if title == "":
            print("warning: you did not specify a title")

    ax.set_title(title, **DEFAULT_TITLE_STYLE)
