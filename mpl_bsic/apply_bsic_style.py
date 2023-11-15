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
This is the examples section. WIP.
"""


def apply_bsic_style(fig: Figure, ax: Axes):
    r"""Apply the BSIC Style to an existing matplotlib plot.

    First, it sets the font family and size for the overall plot
    and the color cycle to use.
    Then, if the plot has a title, then it applies the default title style.

    You must call this function **immediately after creating the figure
    and axes and setting the title**, and in any case before plotting
    (otherwise, colors won't be applied).

    .. warning:: if you want to specify and set a **title** to the plot,
        you can either **set it before**
        or give it to the function as a parameter.
        Otherwise, the correct style won't be applied
        and the title will be in Garamond.
        This is forced by matplotlib (there's no way around it that I know of)
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
        ax.set_title('Cos(x)') # set the title before applying the style
        # the function will re-set the title with the correct style
        apply_bsic_style(fig, ax)

        ax.plot(x,y)
    """
    plt.rcParams["font.sans-serif"] = BSIC_FONT_FAMILY
    plt.rcParams["font.size"] = DEFAULT_FONT_SIZE
    plt.rcParams["axes.prop_cycle"] = DEFAULT_COLOR_CYCLE
    ax.set_prop_cycle(DEFAULT_COLOR_CYCLE)

    def update_title_style(_):
        ax.set_title(ax.get_title(), **DEFAULT_TITLE_STYLE)

        ani.event_source.stop()  # Stop the animation after the first frame

    # if title has already been set, apply the style
    if ax.get_title() != '':
        ax.set_title(ax.get_title(), **DEFAULT_TITLE_STYLE)
    # otherwise, wait for it to get applied and then apply the style
    else:
        ani = FuncAnimation(fig, update_title_style, frames=[0])
        plt.gcf().ani = ani  # to make sure the animation lives until the end

    # set lines colors
    lines = ax.get_lines()
    for line, color in zip(lines, BSIC_COLORS):
        line.set(color=color)
