"""A CLI for fooy. foo-cli does not currently exist in PyPi"""

__version__ = "0.0.0"


import sys

from fooy import do_fooy

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <number of foos>", file=sys.stderr)
        exit(2)

    print(do_fooy(int(sys.argv[1])))
