from matplotlib.figure import Figure


def run_animations(fig: Figure):
    if hasattr(fig, "_bsic_animations"):
        bsic_animations = fig.__getattribute__("_bsic_animations")

        for ani in bsic_animations:
            for _ in range(5):
                try:
                    ani._stop = False
                    ani._step()
                except (
                    AttributeError
                ):  # catches when animation has no more frames and cannot step anymore
                    break
