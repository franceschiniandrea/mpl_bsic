from matplotlib.figure import Figure

from utils.run_animations import run_animations


def export_figure(fig: Figure, filename: str):
    """
    Export a figure according to BSIC Standards.

    First, the function forces the animations to run,
    making sure that any style is applied before exporting.
    Additionally, exports the figure in ``svg`` format,
    with ``bbox_inches='tight'`` and ``dpi=1200``.

    Parameters
    ----------
    fig : Figure
        The ``matplotlib`` figure to export.
    filename : str
        The filename that should be used when exporting.

    See Also
    --------
    mpl_bsic.apply_bsic_style :
        Applies the BSIC Style to plots.

    mpl_bsic.apply_bsic_logo :
        Applies the BSIC Logo to plots.

    Examples
    --------
    .. code-block:: python
        :emphasize-lines: 11

        from mpl_bsic import apply_bsic_style, export_figure

        x = np.linspace(0,10,100)
        y = np.sin(x)

        fig, ax = plt.subplots()
        ax.plot(x,y)
        ax.set_title('Sin(x)')

        apply_bsic_style(fig, ax)
        export_figure(fig, 'output_filename')
    """
    run_animations(fig)

    fig.savefig(filename + ".svg", dpi=1200, bbox_inches="tight")
