from typing import Literal
from matplotlib.figure import Figure
import matplotlib.image as image


def apply_bsic_logo(
    fig: Figure,
    location: Literal[
        "top left", "top right", "bottom left", "bottom right"
    ] = "top left",
    logo_type: Literal["full", "logo"] = "full",
    logo_scale: int = 3,
):
    """WIP - DO NOT USE YET"""

    logo = image.imread(f"mpl_bsic/logos/bsic_logo_formal_{logo_scale}x.png")

    # (x, y, width, height)
    imax = fig.add_axes([0.1, 0.7, 0.2, 0.2])
    # remove ticks & the box from imax
    imax.set_axis_off()
    # print the logo with aspect="equal" to avoid distorting the logo
    imax.imshow(logo, aspect="equal")
