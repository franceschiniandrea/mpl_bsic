import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from tools import baseline_save_fig, image_compare  # noqa

from mpl_bsic import apply_bsic_logo, apply_bsic_style


def _gen_data():
    x = np.linspace(0, 5, 100)
    y = np.sin(x)

    return x, y


class TestLogoTopLeft:
    """Tests when the logo is positioned on the top left corner of the plot"""

    @image_compare(baseline_images="test_logo_top_lx")
    def test_logo_1(self):
        """Tests when the function is called immediately"""
        x, y = _gen_data()

        fig, ax = plt.subplots(1, 1)
        ax: Axes
        apply_bsic_style(fig, ax)
        apply_bsic_logo(fig, ax)

        ax.plot(x, y)
        ax.set_title("Sin(x)")

        return fig

    @image_compare(baseline_images="test_logo_top_lx")
    def test_logo_2(self):
        """Tests when the function gets in the middle"""

        x, y = _gen_data()
        fig, ax = plt.subplots(1, 1)
        ax: Axes

        ax.plot(x, y)
        apply_bsic_style(fig, ax)
        apply_bsic_logo(fig, ax)
        ax.set_title("Sin(x)")

        return fig

    @image_compare(baseline_images="test_logo_top_lx")
    def test_logo_3(self):
        """Tests when the function gets called at the very end"""

        x, y = _gen_data()
        fig, ax = plt.subplots(1, 1)
        ax: Axes

        ax.plot(x, y)
        ax.set_title("Sin(x)")
        apply_bsic_style(fig, ax)
        apply_bsic_logo(fig, ax)

        return fig

    @image_compare(baseline_images="test_logo_top_lx")
    def test_logo_4(self):
        """Logo gets called before style"""

        x, y = _gen_data()
        fig, ax = plt.subplots(1, 1)
        ax: Axes

        ax.plot(x, y)
        ax.set_title("Sin(x)")
        apply_bsic_logo(fig, ax)
        apply_bsic_style(fig, ax)

        return fig


class TestLogoTopRight:
    """Tests when the logo is positioned on the top left corner of the plot"""

    @image_compare(baseline_images="test_logo_top_rx")
    def test_logo_1(self):
        """Tests when the function is called immediately"""
        x, y = _gen_data()

        fig, ax = plt.subplots(1, 1)
        ax: Axes
        apply_bsic_style(fig, ax)
        apply_bsic_logo(fig, ax, location="top right")

        ax.plot(x, y)
        ax.set_title("Sin(x)")

        return fig

    @image_compare(baseline_images="test_logo_top_rx")
    def test_logo_2(self):
        """Tests when the function gets in the middle"""

        x, y = _gen_data()
        fig, ax = plt.subplots(1, 1)
        ax: Axes

        ax.plot(x, y)
        apply_bsic_style(fig, ax)
        apply_bsic_logo(fig, ax, location="top right")
        ax.set_title("Sin(x)")

        return fig

    @image_compare(baseline_images="test_logo_top_rx")
    def test_logo_3(self):
        """Tests when the function gets called at the very end"""

        x, y = _gen_data()
        fig, ax = plt.subplots(1, 1)
        ax: Axes

        ax.plot(x, y)
        ax.set_title("Sin(x)")
        apply_bsic_style(fig, ax)
        apply_bsic_logo(fig, ax, location="top right")

        return fig

    @image_compare(baseline_images="test_logo_top_rx")
    def test_logo_4(self):
        """Logo gets called before style"""

        x, y = _gen_data()
        fig, ax = plt.subplots(1, 1)
        ax: Axes

        ax.plot(x, y)
        ax.set_title("Sin(x)")
        apply_bsic_logo(fig, ax, location="top right")
        apply_bsic_style(fig, ax)

        return fig


class TestLogoBtmLeft:
    """Tests when the logo is positioned on the bottom left corner of the plot"""

    @image_compare(baseline_images="test_logo_btm_lx")
    def test_logo_1(self):
        """Tests when the function is called immediately"""
        x, y = _gen_data()

        fig, ax = plt.subplots(1, 1)
        ax: Axes
        apply_bsic_style(fig, ax)
        apply_bsic_logo(fig, ax, location="bottom left")

        ax.plot(x, y)
        ax.set_title("Sin(x)")

        return fig

    @image_compare(baseline_images="test_logo_btm_lx")
    def test_logo_2(self):
        """Tests when the function gets in the middle"""

        x, y = _gen_data()
        fig, ax = plt.subplots(1, 1)
        ax: Axes

        ax.plot(x, y)
        apply_bsic_style(fig, ax)
        apply_bsic_logo(fig, ax, location="bottom left")
        ax.set_title("Sin(x)")

        return fig

    @image_compare(baseline_images="test_logo_btm_lx")
    def test_logo_3(self):
        """Tests when the function gets called at the very end"""

        x, y = _gen_data()
        fig, ax = plt.subplots(1, 1)
        ax: Axes

        ax.plot(x, y)
        ax.set_title("Sin(x)")
        apply_bsic_style(fig, ax)
        apply_bsic_logo(fig, ax, location="bottom left")

        return fig

    @image_compare(baseline_images="test_logo_btm_lx")
    def test_logo_4(self):
        """Logo gets called before style"""

        x, y = _gen_data()
        fig, ax = plt.subplots(1, 1)
        ax: Axes

        ax.plot(x, y)
        ax.set_title("Sin(x)")
        apply_bsic_logo(fig, ax, location="bottom left")
        apply_bsic_style(fig, ax)

        return fig


class TestLogoBtmRight:
    """Tests when the logo is positioned on the bottom left corner of the plot"""

    @image_compare(baseline_images="test_logo_btm_rx")
    def test_logo_1(self):
        """Tests when the function is called immediately"""
        x, y = _gen_data()

        fig, ax = plt.subplots(1, 1)
        ax: Axes
        apply_bsic_style(fig, ax)
        apply_bsic_logo(fig, ax, location="bottom right")

        ax.plot(x, y)
        ax.set_title("Sin(x)")

        return fig

    @image_compare(baseline_images="test_logo_btm_rx")
    def test_logo_2(self):
        """Tests when the function gets in the middle"""

        x, y = _gen_data()
        fig, ax = plt.subplots(1, 1)
        ax: Axes

        ax.plot(x, y)
        apply_bsic_style(fig, ax)
        apply_bsic_logo(fig, ax, location="bottom right")
        ax.set_title("Sin(x)")

        return fig

    @image_compare(baseline_images="test_logo_btm_rx")
    def test_logo_3(self):
        """Tests when the function gets called at the very end"""

        x, y = _gen_data()
        fig, ax = plt.subplots(1, 1)
        ax: Axes

        ax.plot(x, y)
        ax.set_title("Sin(x)")
        apply_bsic_style(fig, ax)
        apply_bsic_logo(fig, ax, location="bottom right")

        return fig

    @image_compare(baseline_images="test_logo_btm_rx")
    def test_logo_4(self):
        """Logo gets called before style"""

        x, y = _gen_data()
        fig, ax = plt.subplots(1, 1)
        ax: Axes

        ax.plot(x, y)
        ax.set_title("Sin(x)")
        apply_bsic_logo(fig, ax, location="bottom right")
        apply_bsic_style(fig, ax)

        return fig
