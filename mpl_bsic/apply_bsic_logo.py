import os
import sysconfig
from typing import Literal

import matplotlib.image as image
from matplotlib.animation import FuncAnimation
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.offsetbox import AnnotationBbox, OffsetImage

from utils.set_animations import insert_animation

Location = Literal["top left", "top right", "bottom left", "bottom right"]

_ANN_ANCHOR_POINTS = {
    "top left": (0, 1),
    "top right": (1, 1),
    "bottom left": (0, 0),
    "bottom right": (1, 0),
}


def _get_img_path(logo_type: str):
    BASE_DIR = None

    if os.path.isfile(sysconfig.get_path("platlib") + "/mpl_bsic"):
        BASE_DIR = sysconfig.get_path("platlib") + "/mpl_bsic"  # pragma: no cover
    else:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    path = BASE_DIR + "/static/bsic_logo_" + logo_type + "_1x.png"

    return path


def _get_annotation_position(ax: Axes, location: Location, fr: float):
    x0, x1 = ax.get_xbound()
    y0, y1 = ax.get_ybound()

    xlen = x1 - x0
    ylen = y1 - y0

    if location == "bottom left":
        pos = (x0 + xlen / fr, y0 + ylen / fr)
    elif location == "top left":
        pos = (x0 + xlen / fr, y1 - ylen / fr)
    elif location == "top right":
        pos = (x1 - xlen / fr, y1 - ylen / fr)
    elif location == "bottom right":
        pos = (x1 - xlen / fr, y0 + ylen / fr)

    return pos


def apply_bsic_logo(
    fig: Figure,
    ax: Axes,
    scale: float = 0.03,
    location: Location = "top left",
    logo_type: Literal["formal", "square"] = "formal",
    alpha: float = 1,
    closeness_to_border: float = 50,
):
    """Apply the BSIC Logo to the Plot.

    You can specify the scale, location, type, alpha, and how close
    the logo is to the border.
    Since the optimal values for these parameters will value from plot to plot,
    the suggestion is to tweak them until you find the right values for your plot.
    Choose the location so that the plot and logo overlap as little
    as possible.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The Figure instance from matplotlib.
    ax : matplotlib.axes.Axes
        The Axes instance from matplotlib.
    scale : float, optional
        How much to scale the image, by default 0.03.
    location : Location, optional
        The location to use for the logo, by default "top left".
        Can be "top left", "top right", "bottom left", "bottom right".
    logo_type : Literal["formal", "square"], optional
        Specify the logo to use, by default "formal".
        The Formal logo is the extended one,
        the Square logo includes only the square.
    alpha : float, optional
        The alpha to use for the image (if you want transparency),
        by default 1.
    closeness_to_border : float, optional
        How close the logo should be to the border.
        A larger value means the logo will be closer to the border,
        by default 50.

    See Also
    --------
    mpl_bsic.apply_bsic_style :
        Applies the BSIC Style to plots.

    Examples
    --------

    .. plot::
        :alt: example plot using apply_bsic_logo() (top right, formal logo)

        from mpl_bsic import apply_bsic_style, apply_bsic_logo

        import matplotlib.pyplot as plt

        x = np.linspace(0, 5, 100)
        y = np.cos(x)

        fig, ax = plt.subplots(1, 1)
        ax.set_title('Cos(x)') # set the title before applying the style
        apply_bsic_style(fig)
        apply_bsic_logo(fig, ax, location='top right', scale=0.03)

        ax.plot(x,y)
        run_animations(fig) # only needed for the docs, don't call in the actual code

    .. plot::
        :alt: example plot using apply_bsic_logo() (btm left, square logo)

        from mpl_bsic import apply_bsic_style, apply_bsic_logo

        import matplotlib.pyplot as plt

        x = np.linspace(0, 5, 100)
        y = np.cos(x)

        fig, ax = plt.subplots(1, 1)
        ax.set_title('Cos(x)') # set the title before applying the style
        apply_bsic_style(fig)
        apply_bsic_logo(
            fig,
            ax,
            location='bottom left',
            scale=0.05,
            logo_type='square', # use the square logo
            closeness_to_border=25 # make the logo closer to the border
        )

        ax.plot(x,y)
        run_animations(fig) # only needed for the docs, don't call in the actual code
    """

    # gets the path for the logo and reads the image
    image_path = _get_img_path(logo_type)
    logo = image.imread(image_path)

    imagebox = OffsetImage(logo, zoom=scale)
    imagebox.image.set_alpha(alpha)

    # generates the annotation box containing the logo at the correct position
    def gen_logo_annotation_box(position: tuple[float, float]) -> AnnotationBbox:
        """Create the annotation box containing the logo,
        at the correct location (top left, top right, bottom left, bottom right),
        at the correct position on the plot (from the corner).
        """

        ab = AnnotationBbox(
            imagebox,
            position,
            box_alignment=_ANN_ANCHOR_POINTS[location],
            pad=0,
            frameon=False,
            bboxprops=dict(edgecolor="None"),
        )

        return ab

    def logo_animation_func(_):
        position = _get_annotation_position(ax, location, closeness_to_border)

        ab = gen_logo_annotation_box(position)
        new_ab = ax.add_artist(ab)
        return [new_ab]

    logo_animation = FuncAnimation(
        fig,
        logo_animation_func,
        frames=1,  # just one frame
        blit=False,
        cache_frame_data=False,  # to avoid caching the image which causes lag,
        repeat=False,  # to make sure it runs only once when calling plt.show()
    )

    insert_animation(fig, logo_animation)
