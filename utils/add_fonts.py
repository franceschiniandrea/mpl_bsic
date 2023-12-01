import os
import sysconfig
from os.path import dirname
from pathlib import Path

import matplotlib.font_manager as font_manager


def _get_fonts_path():
    BASE_DIR = None

    if os.path.isfile(sysconfig.get_path("platlib") + "/mpl_bsic"):
        BASE_DIR = sysconfig.get_path("platlib") + "/mpl_bsic"  # pragma: no cover
        print("base dir: ", BASE_DIR)
    else:
        BASE_DIR = os.path.join(dirname(dirname(os.path.abspath(__file__))), "mpl_bsic")
        print("base dir: ", BASE_DIR)

    path = os.path.join(BASE_DIR, "fonts")
    print("fonts dir: ", path)

    return path


def add_fonts():
    # first try to find if the fonts are installed
    fontlist = font_manager.get_font_names()
    if "Garamond" in fontlist and "Gill Sans MT" in fontlist:
        print("fonts already added so will not add again")
        return

    # if not, add them
    print("adding fonts to font manager")
    font_path = _get_fonts_path()
    font_families_paths = [
        os.path.join(font_path, family) for family in ["garamond", "gill_sans_mt"]
    ]

    for family_dir in font_families_paths:
        for file in os.listdir(family_dir):
            font_path = Path(family_dir, file)

            font_manager.fontManager.addfont(font_path)
            # print(f"Added font {font_path}.")
            # print(
            #     "font name: ", font_manager.FontProperties(fname=font_path).get_name()
            # )
