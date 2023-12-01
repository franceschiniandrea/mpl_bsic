import os
from os.path import dirname
from pathlib import Path

import matplotlib.font_manager as font_manager


def add_fonts():
    # first try to find if the fonts are installed
    fontlist = font_manager.get_font_names()
    if "Garamond" in fontlist and "Gill Sans MT" in fontlist:
        print("fonts already added so will not add again")
        return

    # if not, add them
    print("adding fonts to font manager")
    package_path = dirname(dirname(os.path.abspath(__file__)))
    font_path = os.path.join(package_path, "fonts")
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
