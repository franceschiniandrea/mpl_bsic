import numpy as np
import test_setup  # noqa
from performance_tester import performance_test


@performance_test(1000, "millis")
def test():
    """test docstring"""
    return (np.random.rand(100000) * 5).sum()


test()
