from mpl_bsic import check_figsize


class TestFigsize:
    def test_invalid_width(self, capfd):
        width = 8
        height = 8

        check_figsize(width, height, aspect_ratio=None)

        out, err = capfd.readouterr()
        print(out, err)
        print(out.split("\n"))
        messages = out.split("\n")

        assert (
            messages[0] == "--- Warning ---"
            and messages[1] == "Width is greater than 7.32 inches."
        )

    # TODO this test is invalid since the function is invalid
    # def test_unspecified_width(self, capfd):
    #     width = None
    #     height = 8

    #     check_figsize(width, height, aspect_ratio=None)

    #     out, err = capfd.readouterr()
    #     print(out, err)
    #     print(out.split("\n"))
    #     messages = out.split("\n")

    #     assert (
    #         messages[0] == "you did not specify width."
    #         and messages[1] == "Defaulting to 7.32 inches (width of a word document))"
    #     )

    def test_correct_width(self):
        width = 7.32
        height = 8

        width_ret, height_ret = check_figsize(width, height, aspect_ratio=None)

        assert width_ret == width and height_ret == height

    def test_unspecified_height(self):
        width = 7.32
        height = None
        aspect_ratio = 16 / 9

        width_ret, height_ret = check_figsize(width, height, aspect_ratio)

        assert width_ret == width and height_ret - width * aspect_ratio < 1e-5
