from cycler import cycler
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.axes import Axes
from matplotlib.figure import Figure

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
This is the examples section. TODO.
"""


def apply_bsic_style(fig: Figure, ax: Axes):
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

    .. warning:: You have to make sure you always call ``plt.show()``,
        even if you just want to export the figure. This makes sure
        that the animation is performed and the correct style is applied to the title.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Matplotlib Figure instance.
    ax : matplotlib.axes.Axes
        Matplotlib Axes instance.

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
    """

    # sets font family, size, and cycler to rcparams
    plt.rcParams["font.sans-serif"] = BSIC_FONT_FAMILY
    plt.rcParams["font.size"] = DEFAULT_FONT_SIZE
    plt.rcParams["axes.prop_cycle"] = DEFAULT_COLOR_CYCLE
    ax.set_prop_cycle(DEFAULT_COLOR_CYCLE)

    # function to animate the styling of the title
    def update_title_style(_):
        ax.set_title(ax.get_title(), **DEFAULT_TITLE_STYLE)

        ani.event_source.stop()  # Stop the animation after the first frame

    # if title has already been set, apply the style
    if ax.get_title() != "":
        ax.set_title(ax.get_title(), **DEFAULT_TITLE_STYLE)
    # otherwise, wait for it to get applied and then apply the style
    else:
        ani = FuncAnimation(
            fig, update_title_style, frames=1, blit=False  # type: ignore
        )
        # to make sure the animation lives until the end
        fig.__setattr__("ani", ani)

    # set lines colors if already plotted
    lines = ax.get_lines()
    for line, color in zip(lines, BSIC_COLORS):
        line.set(color=color)

    # set legend colors if already plotted
    if ax.get_legend() is not None:
        ax.legend()
