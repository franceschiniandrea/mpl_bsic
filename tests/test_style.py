from matplotlib.axes import Axes
import numpy as np
import matplotlib.pyplot as plt
from mpl_bsic import apply_bsic_style, apply_bsic_logo
import pytest
import os


class TestStyle:
    @pytest.mark.mpl_image_compare
    def test_style(self):
        print("CWD: ", os.getcwd())

        x = np.linspace(0, 5, 100)
        y = np.sin(x)

        fig, ax = plt.subplots(1, 1)
        apply_bsic_logo(fig, ax, location="top right", scale=0.03, logo_type="formal")
        ax: Axes
        apply_bsic_style(fig, ax)

        ax.plot(x, y)

        ax.set_title("Sin(x)")
        fig.show()
        return fig
