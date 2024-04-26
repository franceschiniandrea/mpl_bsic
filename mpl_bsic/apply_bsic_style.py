from typing import Union

import numpy as np

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from utils.add_fonts import add_fonts
from utils.set_animations import insert_animation
from .constants import FONTSIZES, TITLE_STYLE, COLOR_CYCLE, BSIC_COLORS, FONTFAMILIES


def _style_axis(fig: Figure, ax: Axes):
    if not isinstance(fig, Figure):
        raise Exception('The first parameter in _style_axis must be an instance of Figure')
    if not isinstance(ax, Axes):
        raise Exception('The second parameter in _style_axis must be an instance of Axes')

    # set the color cycle for the axis
    ax.set_prop_cycle(COLOR_CYCLE)

    def update_title_anim(_):
        ax.set_title(ax.get_title(), **TITLE_STYLE)

        return ax.artists

    # if title has already been set, apply the style
    if ax.get_title() != "":
        ax.set_title(ax.get_title(), **TITLE_STYLE)
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


def _fill_between(ax: Axes, alpha: float):
    lines = ax.get_lines()
    for line in lines:
        color = line.get_color()
        x = line.get_xdata()
        y = line.get_ydata()

        ax.fill_between(x,y,color=color, alpha=alpha)


def apply_bsic_style(
    fig: Figure,
    ax: Union[Axes, np.ndarray] = None,
    sources: Union[str, list[str]] = "BSIC",
    fill_between: bool = False,
    fill_between_alpha: float = 0.25
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

        .. deprecated:: 1.3.2
            The ``ax`` parameter will be removed in a future release, since it is not needed anymore.
            ``apply_bsic_style`` now gets all the axes from the figure instance (and is capable
            of styling all the axes at once), thus it is
            not necessary to include the axes in the function call anymore.

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
    fill_between : bool, optional
        If true, it colors the area between each line and the 0 axis in the plot.
        The fill is consistent with the color of each line, and you can specify
        the alpha to use in the next parameter. Defaults to ``False``.

        .. versionadded:: 1.3.2
    fill_between_alpha : float, optional
        The alpha value to use when ``fill_between`` is set to ``True``.
        Defaults to 0.25.

        .. versionadded:: 1.3.2

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
        ax.set_title('Cos(x)')
        apply_bsic_style(fig, sources=['Bloomberg'])

        ax.plot(x,y)

    .. plot::

        from mpl_bsic import apply_bsic_style

        x = np.linspace(0, 5, 100)
        y = np.cos(x)

        fig, ax = plt.subplots(1, 1)
        ax.set_title('Cos(x)') # set the title before applying the style
        # the function will re-set the title with the correct style
        apply_bsic_style(fig, ax, sources=['Bloomberg', 'FactSet'])

        ax.plot(x,y)
        apply_bsic_style(fig, fill_between=True)
    """
    add_fonts()

    # sets font family, size, and cycler to rcparams
    plt.rcParams["font.sans-serif"] = FONTFAMILIES.TEXT.value
    plt.rcParams["font.size"] = FONTSIZES.TEXT.value
    plt.rcParams["axes.prop_cycle"] = COLOR_CYCLE

    # to make sure the figure is saved correctly
    # plt.rcParams["savefig.bbox"] = "tight" # remove to make add_title_subtitle work
    plt.rcParams["savefig.dpi"] = 1200

    # apply style to suptitle
    if hasattr(fig, "get_suptitle") and fig.get_suptitle() != "":
        fig.suptitle(fig.get_suptitle(), **TITLE_STYLE)

    # check that axes is not specified anymore
    #   otherwise issue a DeprecationWarning
    if ax is not None:
        raise DeprecationWarning(
            'The parameter `ax` is not necessary anymore, \nand it will be removed in a future version.\n'
            'The library gets all the axis in the figure through the `fig` parameter.'
        )

    axes = fig.axes
    for ax in axes:
        _style_axis(fig, ax)

        # TODO FIX: fill between is not applied if ax.plot is called after apply_bsic_style
        if fill_between:
            _fill_between(ax, fill_between_alpha)
    # add sources to plot
    _add_sources(fig, sources)
