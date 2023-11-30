from mpl_bsic import check_figsize


class TestFigsize:
    def test_invalid_width(self, caplog):
        width = 8
        height = 8

        w, h = check_figsize(width, height)

        assert "WARNING" in caplog.text
        assert "Width is greater than 7.32 inches" in caplog.text

        assert w == 7.32 and h == 7.32

    def test_unspecified_width(self):
        width = None
        height = 8
        aspect_ratio = 16 / 9

        w, h = check_figsize(width, height, aspect_ratio)

        assert w == height / aspect_ratio and h == 8

    def test_correct_width(self):
        width = 7.32
        height = 8

        w, h = check_figsize(width, height)

        assert w == width and h == height

    def test_width_and_aspectratio(self):
        width = 7.32
        height = None
        aspect_ratio = 16 / 9

        w, h = check_figsize(width, height, aspect_ratio)

        assert w == width and h - width * aspect_ratio < 1e-5

    def test_unspecified_height_err(self):
        width = 7.32
        height = None
        aspect_ratio = None

        try:
            check_figsize(width, height, aspect_ratio)
        except Exception as e:
            assert "you must specify aspect_ratio and width" in str(e).lower()

    def test_no_paramters(self):
        try:
            check_figsize()
        except Exception as e:
            assert "You must specify at least two of the three parameters" in str(e)
