import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from tools import image_compare

from mpl_bsic import apply_bsic_style


def _gen_data():
    x = np.linspace(0, 5, 100)
    y = np.sin(x)

    return x, y


class TestStyle:
    @image_compare(baseline_images="test_style_1")
    def test_style_1(self):
        """Tests when the function gets called immediately"""
        x, y = _gen_data()

        fig, ax = plt.subplots(1, 1)
        ax: Axes
        apply_bsic_style(fig, ax)

        ax.plot(x, y)
        ax.set_title("Sin(x)")

        return fig

    @image_compare(baseline_images="test_style_1")
    def test_style_2(self):
        """Tests when the function gets in the middle"""

        x, y = _gen_data()
        fig, ax = plt.subplots(1, 1)
        ax: Axes

        ax.plot(x, y)
        apply_bsic_style(fig, ax)
        ax.set_title("Sin(x)")

        return fig

    @image_compare(baseline_images="test_style_1")
    def test_style_3(self):
        """Tests when the function gets called at the very end"""

        x, y = _gen_data()
        fig, ax = plt.subplots(1, 1)
        ax: Axes

        ax.plot(x, y)
        ax.set_title("Sin(x)")
        apply_bsic_style(fig, ax)

        return fig

    @image_compare(baseline_images="test_style_legend")
    def test_style_legend_1(self):
        """Tests when the style gets applied to a figure with a legend,
        before applying style"""

        x, y = _gen_data()
        fig, ax = plt.subplots(1, 1)
        ax: Axes

        ax.plot(x, y, label="Sin(x)")
        ax.set_title("Sin(x)")
        ax.legend()
        apply_bsic_style(fig, ax)

        return fig

    @image_compare(baseline_images="test_style_legend")
    def test_style_legend_2(self):
        """Tests when the style gets applied to a figure with a legend,
        after applying style"""

        x, y = _gen_data()
        fig, ax = plt.subplots(1, 1)
        ax: Axes

        ax.plot(x, y, label="Sin(x)")
        ax.set_title("Sin(x)")
        apply_bsic_style(fig, ax)
        ax.legend()

        return fig
