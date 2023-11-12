"""Path hack to make tests work."""

import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")
