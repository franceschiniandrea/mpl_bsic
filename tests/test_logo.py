from matplotlib.axes import Axes
import numpy as np
import matplotlib.pyplot as plt
from tools import image_compare

import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")
from mpl_bsic import apply_bsic_style, apply_bsic_logo


x = np.linspace(0, 5, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots(1, 1)
apply_bsic_logo(fig, ax)

ax.plot(x, y1, label="sin(x)")
ax.plot(x, y2, label="cos(x)")
ax.set_title("BSIC Styling Library")
ax.legend()
apply_bsic_style(fig, ax)
fig.savefig("test_logo.svg", dpi=1200, bbox_inches="tight")
plt.show()
