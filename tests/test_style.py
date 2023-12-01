import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from tools import baseline_save_fig, image_compare  # noqa

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

    @image_compare(baseline_images="test_style_multiple_axs")
    def test_multiple_axs_1(self):
        """Tests when the function gets called
        with a figure that has more than one axis
        """

        x, y = _gen_data()
        fig, axs = plt.subplots(1, 2)

        apply_bsic_style(fig, axs)

        ax0, ax1 = axs
        ax0: Axes
        ax1: Axes

        ax0.set_title("Sin(x) 1")
        ax0.plot(x, y)
        ax1.set_title("Sin(x) 2")
        ax1.plot(x, y)

        return fig

    @image_compare(baseline_images="test_style_multiple_axs")
    def test_multiple_axs_2(self):
        """Tests when the function gets called
        with a figure that has more than one axis
        """

        x, y = _gen_data()
        fig, axs = plt.subplots(1, 2)

        ax0, ax1 = axs
        ax0: Axes
        ax1: Axes

        ax0.set_title("Sin(x) 1")
        ax0.plot(x, y)
        ax1.set_title("Sin(x) 2")
        ax1.plot(x, y)

        apply_bsic_style(fig, axs)

        return fig

    @image_compare(baseline_images="test_style_multiple_sources")
    def test_multiple_sources_1(self):
        x, y = _gen_data()
        fig, axs = plt.subplots(1, 2)

        ax0, ax1 = axs
        ax0: Axes
        ax1: Axes

        ax0.set_title("Sin(x) 1")
        ax0.plot(x, y)
        ax1.set_title("Sin(x) 2")
        ax1.plot(x, y)

        apply_bsic_style(fig, axs, sources=["BSIC", "Bloomberg"])

        return fig

    @image_compare(baseline_images="test_style_multiple_sources")
    def test_multiple_sources_2(self):
        x, y = _gen_data()
        fig, axs = plt.subplots(1, 2)

        ax0, ax1 = axs
        ax0: Axes
        ax1: Axes

        ax0.set_title("Sin(x) 1")
        ax0.plot(x, y)
        ax1.set_title("Sin(x) 2")
        ax1.plot(x, y)

        apply_bsic_style(fig, axs, sources=["Bloomberg"])

        return fig

    @image_compare(baseline_images="test_style_multiple_sources")
    def test_multiple_sources_3(self):
        x, y = _gen_data()
        fig, axs = plt.subplots(1, 2)

        ax0, ax1 = axs
        ax0: Axes
        ax1: Axes

        ax0.set_title("Sin(x) 1")
        ax0.plot(x, y)
        ax1.set_title("Sin(x) 2")
        ax1.plot(x, y)

        apply_bsic_style(fig, axs, sources="Bloomberg")

        return fig

    @image_compare(baseline_images="test_style_single_source")
    def test_single_source_1(self):
        x, y = _gen_data()
        fig, axs = plt.subplots(1, 2)

        ax0, ax1 = axs
        ax0: Axes
        ax1: Axes

        ax0.set_title("Sin(x) 1")
        ax0.plot(x, y)
        ax1.set_title("Sin(x) 2")
        ax1.plot(x, y)

        apply_bsic_style(fig, axs, sources="BSIC")

        return fig

    @image_compare(baseline_images="test_style_single_source")
    def test_single_source_2(self):
        x, y = _gen_data()
        fig, axs = plt.subplots(1, 2)

        ax0, ax1 = axs
        ax0: Axes
        ax1: Axes

        ax0.set_title("Sin(x) 1")
        ax0.plot(x, y)
        ax1.set_title("Sin(x) 2")
        ax1.plot(x, y)

        apply_bsic_style(fig, axs, sources=["BSIC"])

        return fig

    @image_compare(baseline_images="test_style_single_source")
    def test_single_source_3(self):
        x, y = _gen_data()
        fig, axs = plt.subplots(1, 2)

        ax0, ax1 = axs
        ax0: Axes
        ax1: Axes

        ax0.set_title("Sin(x) 1")
        ax0.plot(x, y)
        ax1.set_title("Sin(x) 2")
        ax1.plot(x, y)

        apply_bsic_style(fig, axs)

        return fig
