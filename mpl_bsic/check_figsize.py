def check_figsize(
    width: float, height: float | None, aspect_ratio: float | None
) -> tuple[float, float]:
    r"""Check the validity of the figsize.

    Checks the validity of the figsize parameters
    and returns the width and height to use.

    Parameters
    ----------
    width : float
        Width of the Figure, in inches.
    height : float | None
        Height of the Figure, in inches.
    aspect_ratio : float | None
        Aspect Ratio of the figure, as a float.
        E.g. 16/9 for 16:9 aspect ratio.

    Returns
    -------
    tuple[float, float]
        The width and height to use for the Figure.

    See Also
    --------
    apply_bsic_style.apply_bsic_style :
        The function that applies the style to the plot.
    mpl_bsic.preprocess_dataframe :
        The function that preprocesses the DataFrame before plotting.

    Examples
    --------
    This is the examples section. WIP.
    """
    if width > 7.32:
        print("--- Warning ---")
        print(
            """Width is greater than 7.32 inches.
This is the width of a word document available for figures.
If you set the width > 7.32, the figure will be resized in word and
the font sizes will not be consistent across the article and the graph"""
        )

    if width is None:
        print(
            """you did not specify width.
            Defaulting to 7.32 inches (width of a word document))"""
        )

    if height is None:
        if aspect_ratio is None:
            raise Exception("You must specify either height or aspect_ratio")

        height = width * aspect_ratio

    return width, height
