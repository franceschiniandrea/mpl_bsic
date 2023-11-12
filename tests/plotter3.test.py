from matplotlib.axes import Axes
import numpy as np
import matplotlib.pyplot as plt
import test_setup  # noqa
from mpl_bsic import apply_bsic_style
from mpl_bsic import apply_bsic_logo

x = np.linspace(0, 5, 100)
y = np.sin(x)

fig, ax = plt.subplots(1, 1)
ax: Axes
apply_bsic_style(fig, ax, "Sin(x)")
apply_bsic_logo(fig, x=1)

ax.plot(x, y)

plt.show()
