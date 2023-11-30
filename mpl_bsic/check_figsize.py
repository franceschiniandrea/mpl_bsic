import logging
from numbers import Number
from typing import Optional

log = logging.getLogger("mpl_bsic")


def check_figsize(
    width: Optional[float] = None,
    height: Optional[float] = None,
    aspect_ratio: Optional[float] = None,
) -> tuple[float, float]:
    r"""Check the validity of the figsize.

    Checks the validity of the figsize parameters
    and returns the width and height you should use for the plot.
    You must specify at least two of the three parameters,
    otherwise the function will return an error.

    When exporting plots for a word document, Word will resize the image automatically
    if it doesn't fit the page. This will cause the font sizes to be inconsistent
    across the article and the graph, with the title of the plot being
    smaller than the usual style of the sections.
    To avoid this, you must make sure that the width of the plot is
    **less than 7.32 inches**,
    which is the width of a word document available for figures.

    This function makes sure that you respect the guidelines for the image size,
    so that it won't be later resized by Word and the font sizes will be consistent.

    Parameters
    ----------
    width : float | None
        Width of the Figure, in inches.
    height : float | None
        Height of the Figure, in inches.
    aspect_ratio : float | None
        Aspect Ratio of the figure, as a float.
        E.g. 16/9 for 16:9 aspect ratio.

    Returns
    -------
    tuple[float, float]
        The *correct* width and height to use for the Figure.

    See Also
    --------
    apply_bsic_style.apply_bsic_style :
        The function that applies the style to the plot.
    mpl_bsic.preprocess_dataframe :
        The function that preprocesses the DataFrame before plotting.

    Examples
    --------
    >>> check_figsize(5, 3) # with correct width and height
    (5, 3)

    If the width is too large, it will be resized to fit a word document,
    while keeping the original aspect ratio constant.

    >>> check_figsize(10, 5) # width > 7.32
    Width is greater than 7.32 inches.
    This is the width of a word document available for figures.
    If you set the width > 7.32, the figure will be resized in word and
    the font sizes will not be consistent across the article and the graph
    (7.32, 3.66)

    You can also only specify width/height and aspect ratio,
    and the other will be computed. Again, if the width is too large,
    it will be resized to fit a word document.

    >>> check_figsize(5, aspect_ratio=16/9) # provide width and aspect ratio
    (5, 2.8125)
    >>> check_figsize(10, aspect_ratio=16/9) # width is too large
    Width is greater than 7.32 inches (the max length of a word document).
    Setting width to 7.32 inches.
    (7.32, 4.1175)
    >>> check_figsize(height=3, aspect_ratio=16/9)
    (5.33, 3)
    """

    if all([height is None, width is None, aspect_ratio is None]):
        raise Exception("You must specify at least two of the three parameters")

    # if you specified only width and aspect_ratio
    if height is None:
        if not (isinstance(width, Number) and isinstance(aspect_ratio, Number)):
            raise Exception(
                "If you do not specify height, you must specify aspect_ratio and width"
            )

        if width > 7.32:
            log.warning(
                "Width is greater than 7.32 inches (the max length of a word document). Setting width to 7.32 inches."  # noqa: E501
            )

            width = 7.32

        height = width / aspect_ratio
        return width, height

    # if you specified only height and aspect_ratio
    if width is None:
        if not (isinstance(height, Number) and isinstance(aspect_ratio, Number)):
            raise Exception(
                "If you do not specify width, you must specify aspect_ratio and height"
            )

        width = height * aspect_ratio

        # if > 7.32, set to 7.32 and recompute height
        if width > 7.32:
            log.warning(
                "Width is greater than 7.32 inches (the max length of a word document). Setting width to 7.32 inches."  # noqa: E501
            )

            width = 7.32
            height = width / aspect_ratio

        return width, height

    if width > 7.32:
        log.warning(
            """Width is greater than 7.32 inches.
This is the width of a word document available for figures.
If you set the width > 7.32, the figure will be resized in word and
the font sizes will not be consistent across the article and the graph"""
        )
        log.info("Resizing to fit a word document")

        aspect_ratio = height / width
        width = 7.32
        height = width * aspect_ratio

    return width, height
