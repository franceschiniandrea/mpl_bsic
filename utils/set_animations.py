from matplotlib.animation import Animation
from matplotlib.figure import Figure


def insert_animation(fig: Figure, animation: Animation):
    if hasattr(fig, "_bsic_animations"):
        animations = getattr(fig, "_bsic_animations")
        animations.append(animation)
    else:
        # initialize the animation
        animations = [animation]
        setattr(fig, "_bsic_animations", animations)
