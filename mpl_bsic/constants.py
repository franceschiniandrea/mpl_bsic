from cycler import cycler
import matplotlib.colors as mcolors
from enum import IntEnum, Enum

class FONTSIZES(IntEnum):
    TEXT = 10
    TITLE = 14
    SUBTITLE = 12

class FONTFAMILIES(Enum):
    TITLE = 'Gill Sans MT'
    TEXT = 'Garamond'

class FONTWEIGHTS(Enum):
    TITLE = 600
    SUBTITLE = 500
    TEXT = 400

TITLE_STYLE = {
    "fontname": FONTFAMILIES.TITLE.value,
    "color": "black",
    "fontweight": FONTWEIGHTS.TITLE.value,
    "fontstyle": "italic",
    "fontsize": FONTSIZES.TITLE.value,
}

SUBTITLE_STYLE = {
    'fontname': FONTFAMILIES.TITLE.value,
    'color': 'black',
    'fontweight': FONTWEIGHTS.SUBTITLE.value,
    'fontstyle': 'italic',
    'fontsize': FONTSIZES.SUBTITLE.value
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
COLOR_CYCLE = cycler(color=BSIC_COLORS)

bsic_cmap = mcolors.LinearSegmentedColormap.from_list(
    "bsic", ["#8EC6FF", "#38329A", "#0E0B54", "#601E66"]
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
