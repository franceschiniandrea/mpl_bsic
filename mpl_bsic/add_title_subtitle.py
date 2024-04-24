from matplotlib.figure import Figure
from matplotlib.axes import Axes
from .constants import SUBTITLE_STYLE, TITLE_STYLE
import numpy as np
from utils.logger import get_logger

logger = get_logger(__name__)


def add_title_subtitle(fig: Figure, title: str, subtitle: str, wrapping_factor: float = 0.8):
    axes = fig.axes

    # remove suptitles and titles from the plot
    if fig.get_suptitle() != '':
        fig.suptitle('')
    for ax in axes:
        ax.set_title('')

    # get the left-upper axis to anchor the text to the top left corner
    # if it was created with subplots, it will be a numpy ndarray/list
    if isinstance(axes, np.ndarray):
        if axes.ndim == 1:
            ax = axes[0]
        elif axes.ndim == 2:
            ax = axes[0,0]
        else:
            raise Exception(f'unrecognized dimension of axes = {axes.ndim}')
    elif isinstance(axes, list):
        ax = axes[0]
    # if it is a single plot, it will just be an axes instance
    elif isinstance(axes, Axes):
        ax = axes
    else:
        raise Exception(f'unrecognized axes type = {type(axes)}')

    # parameters to fix the text to the top left corner
    annotate_params = {
        'xy': (0,1),  # in the top left corner of the ax
        'xycoords': ax.get_yaxis_transform(),  # based on ax coordinates
        'textcoords': 'offset points',  # with offset points
        'ha': 'left',
        'va': 'bottom',
        'wrap': True,  # wrapping lines
    }
    bbox_params = {
        'pad': 0,
        'alpha': 0
    }

    # draw the subtitle annotation
    subtitle_bottom_margin = 20  # give it a bit of distance from the top
    subtitle_xytext = (0, subtitle_bottom_margin) # define position of subtitle
    subtitle_annotation = ax.annotate(
        subtitle,
        xytext=subtitle_xytext,
        **annotate_params,
        **SUBTITLE_STYLE,
        bbox=bbox_params)

    # define resize function to resize
    #   based on the current fig width
    def resize():
        new_size = fig.bbox.width * wrapping_factor
        logger.debug(f'Resizing happening - figwidth is {int(fig.bbox.width)}px, resizing bbox to {int(new_size)}px')
        return new_size

    subtitle_annotation._get_wrap_line_width = resize

    # get the final subtitle bbox height and
    #   position the title slightly above it
    subtitle_height = subtitle_annotation.get_window_extent().height
    title_xytext = (0, subtitle_height + 15)

    # create the title annotation
    title_annotation = ax.annotate(title, xytext=title_xytext, **annotate_params, **TITLE_STYLE, bbox=bbox_params)

    # return the two annotation instances
    return title_annotation, subtitle_annotation
