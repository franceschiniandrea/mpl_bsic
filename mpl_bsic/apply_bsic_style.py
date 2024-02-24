from typing import Union

import numpy as np
from cycler import cycler
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from utils.add_fonts import add_fonts
from utils.set_animations import insert_animation

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

BSIC_COLORS = ["#38329A", "#8EC6FF", "#601E66", "#2F2984", "#0E0B54"]
DEFAULT_COLOR_CYCLE = cycler(color=BSIC_COLORS)
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


def _style_axis(fig: Figure, ax: Axes):
    ax.set_prop_cycle(DEFAULT_COLOR_CYCLE)

    def update_title_anim(_):
        ax.set_title(ax.get_title(), **DEFAULT_TITLE_STYLE)

        return ax.artists

    # if title has already been set, apply the style
    if ax.get_title() != "":
        ax.set_title(ax.get_title(), **DEFAULT_TITLE_STYLE)
    # otherwise, wait for it to get applied and then apply the style
    else:
        ani = FuncAnimation(
            fig,
            update_title_anim,
            frames=1,
            blit=False,
            cache_frame_data=False,
            repeat=False,
        )

        insert_animation(fig, ani)

    # set line colors if already plotted
    lines = ax.get_lines()
    for line, color in zip(lines, BSIC_COLORS):
        line.set(color=color)

    # set legend colors if already plotted
    if ax.get_legend() is not None:
        ax.legend()


def _add_sources(fig: Figure, sources: Union[str, list[str]]):
    txt = ""

    # if a single source which is not BSIC, add BSIC
    if isinstance(sources, str) and sources != "BSIC":
        sources = ["BSIC", sources]

    if isinstance(sources, str):
        txt = f"Source: {sources}"

    else:
        # if BSIC is not the first source, insert it
        if "BSIC" not in sources:
            sources.insert(0, "BSIC")
        txt += "Sources: " if len(sources) > 1 else "Source: "

        for i, source in enumerate(sources):
            txt += source
            if i != len(sources) - 1:
                txt += ", "

    # add the text to the figure
    fig.text(0.5, 0, txt, ha="center")


def apply_bsic_style(
    fig: Figure, ax: Union[Axes, np.ndarray], sources: Union[str, list[str]] = "BSIC"
):
    r"""Apply the BSIC Style to an existing matplotlib plot.

    You can call this function at any point in your code, the BSIC style will be applied
    regardless. Before saving, however, make sure you do ``plt.show()``
    so that the style gets applied to the plot.
    This function works by adding an animation such that,
    regardless of where you specify your title,
    it will be updated with the correct style.

    First, the function will set the correct fontsizes
    and font family for the plot text (labels, ticks...).

    It will also set the color cycle used in matplotlib to the colors
    specified in the BSIC design standards.
    If you already plotted, it will, again,
    change the colors of the lines to the correct ones.

    The function will make sure that, whenever you update the title of the plot,
    it gets drawn with the correct style.

    Additionally, it will display the sources specified in the parameter
    at the bottom of the figure.
    It will always add BSIC as a source.

    .. warning:: You have to make sure you always call ``plt.show()``,
        even if you just want to export the figure. This makes sure
        that the animation is performed and the correct style is applied to the title.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Matplotlib Figure instance.
    ax : matplotlib.axes.Axes
        Matplotlib Axes instance.
    sources : str | list[str], optional
        List of sources, by default "BSIC".
        You can either specify a string (if you have only one source)
        or a list of strings (multiple sources).

        Since BSIC is always a source, it will always be included.

        **NB**: if when calling ``plt.show()`` the text seems cutted out, don't worry.
        When exporting using ``bbox_inches="tight"``,
        it will seamlessly fit within the figure.
        This happens because I want to make sure
        there is enough space between the plot and the sources text,
        so I position the text at the very bottom of the figure.

    See Also
    --------
    mpl_bsic.apply_bsic_logo :
        Applies the BSIC Logo to plots.

    Examples
    --------

    .. plot::

        from mpl_bsic import apply_bsic_style

        x = np.linspace(0, 5, 100)
        y = np.cos(x)

        fig, ax = plt.subplots(1, 1)
        ax.set_title('Cos(x)') # set the title before applying the style
        # the function will re-set the title with the correct style
        apply_bsic_style(fig, ax)

        ax.plot(x,y)

    Plotting sources is as easy as specifying the parameter.

    .. plot::

        from mpl_bsic import apply_bsic_style

        x = np.linspace(0, 5, 100)
        y = np.cos(x)

        fig, ax = plt.subplots(1, 1)
        ax.set_title('Cos(x)') # set the title before applying the style
        # the function will re-set the title with the correct style
        apply_bsic_style(fig, ax, sources=['Bloomberg', 'FactSet'])

        ax.plot(x,y)
    """
    add_fonts()

    # sets font family, size, and cycler to rcparams
    plt.rcParams["font.sans-serif"] = "Garamond"
    plt.rcParams["font.size"] = DEFAULT_FONT_SIZE
    plt.rcParams["axes.prop_cycle"] = DEFAULT_COLOR_CYCLE

    # to make sure the figure is saved correctly
    plt.rcParams["savefig.bbox"] = "tight"
    plt.rcParams["savefig.dpi"] = 1200

    # apply style to suptitle
    if hasattr(fig, "get_suptitle") and fig.get_suptitle() != "":
        fig.suptitle(fig.get_suptitle(), **DEFAULT_TITLE_STYLE)

    if isinstance(ax, Axes):
        _style_axis(fig, ax)
    else:
        for axis in ax:
            axis: Axes
            _style_axis(fig, axis)

    # add sources to plot
    _add_sources(fig, sources)
