import conftest  # noqa
import matplotlib.pyplot as plt
import numpy as np

from mpl_bsic import apply_bsic_logo, apply_bsic_style

x = np.linspace(0, 5, 100)
y = np.cos(x)

fig, ax = plt.subplots(1, 1)

apply_bsic_style(fig, ax)
apply_bsic_logo(fig, ax)
ax.set_title("Cos(x)")  # set the title before applying the style

ax.plot(x, y)

plt.show()
