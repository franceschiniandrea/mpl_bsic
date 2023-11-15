import test_setup  # noqa
from matplotlib.axes import Axes
import numpy as np
import matplotlib.pyplot as plt
from mpl_bsic import apply_bsic_style
from mpl_bsic import apply_bsic_logo

x = np.linspace(0, 5, 100)
y = np.sin(x)

fig, ax = plt.subplots(1, 1)
ax: Axes
apply_bsic_style(fig, ax)

ax.plot(x, y)
apply_bsic_logo(ax, location='top left', scale=0.03, logo_type='formal')

ax.set_title('Sin(x)')
plt.show()
