import test_setup  # noqa
from matplotlib.axes import Axes
import numpy as np
import matplotlib.pyplot as plt
from mpl_bsic import apply_bsic_style
from mpl_bsic import apply_bsic_logo

x = np.linspace(0, 5, 100)
y = np.sin(x)

fig, ax = plt.subplots(1, 1)
apply_bsic_logo(fig, ax, location='top right', scale=0.03, logo_type='formal')
ax: Axes
apply_bsic_style(fig, ax)

ax.plot(x, y)

ax.set_title('Sin(x)')
plt.show()
fig.savefig('test.png', dpi=1200)

print(*ax.artists)
