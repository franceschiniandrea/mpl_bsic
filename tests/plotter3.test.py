import matplotlib.pyplot as plt
import numpy as np
import test_setup  # noqa
from matplotlib.axes import Axes

from mpl_bsic import apply_bsic_logo, apply_bsic_style

x = np.linspace(0, 5, 100)
y = np.sin(x)

fig, ax = plt.subplots(
    1,
    1,
)

fig.set_size_inches(7.32, 5)
ax: Axes
apply_bsic_style(fig, ax, "Sin(x)")

ax.plot(x, y)
apply_bsic_logo(ax, location="top right", scale=0.03, logo_type="formal")
plt.show()
