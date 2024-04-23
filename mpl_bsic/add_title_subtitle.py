from matplotlib.figure import Figure
from matplotlib.axes import Axes
from .constants import SUBTITLE_STYLE, TITLE_STYLE
import numpy as np
def add_title_subtitle(fig: Figure, title: str, subtitle: str):
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
        'xy': (0,1),
        'xycoords': ax.get_yaxis_transform(),
        'textcoords': 'offset points',
        'ha': 'left',
        'va': 'bottom',
        'wrap': True,
    }
    bbox_params = {
        'pad': 0,
        'alpha': 0
    }

    # draw the subtitle annotation
    subtitle_bottom_margin = 20
    subtitle_xytext = (0, subtitle_bottom_margin) # define position of subtitle
    subtitle_annotation = ax.annotate(subtitle, xytext=subtitle_xytext, **annotate_params, **SUBTITLE_STYLE, bbox=bbox_params)

    # apply the maximum wrap width to the subtitle (TODO fix)
    max_wrap_width = fig.bbox.width * 0.75
    # subtitle_annotation._get_wrap_line_width = lambda: max_wrap_width
    # subtitle_annotation._get_wrap_line_width = lambda: 600

    # get the height of the subtitle and decide the margin of the title accordingly
    # print(f'new width lim: {max_wrap_width}')
    # print(f'subtitle_annotation height = {subtitle_height}, ')

    # get the subtitle bbox height, and set the position of the title slightly above it
    subtitle_height = subtitle_annotation.get_window_extent().height
    title_xytext = (0, subtitle_height + 15)
    # print(f'new text pos = {title_xytext}')

    # create the title annotation
    title_annotation = ax.annotate(title, xytext=title_xytext, **annotate_params, **TITLE_STYLE, bbox=bbox_params)

    # return the two annotations (TODO remove?)
    return subtitle_annotation, title_annotation
