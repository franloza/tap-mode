"""Main entrypoint of the application for debugging purposes"""

import sys
from tap_mode.tap import TapMode

if __name__ == '__main__':
    TapMode.cli(sys.argv[1:])
