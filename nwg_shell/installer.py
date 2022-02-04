#!/usr/bin/python3

"""
This is going to be the nwg-shell installer, but it's in 5% ready. Please come back later.
"""

import os
import sys
import argparse

from nwg_shell.__about__ import __version__

config_home = os.getenv('XDG_CONFIG_HOME') if os.getenv('XDG_CONFIG_HOME') else os.path.join(os.getenv("HOME"),
                                                                                             ".config")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a",
                        "--all",
                        action="store_true",
                        help="Install/overwrite all configs and styles w/o confirmation")
    parser.add_argument("-v",
                        "--version",
                        action="version",
                        version="%(prog)s version {}".format(__version__),
                        help="display version information")
    args = parser.parse_args()

    print("nwg-shell version {}\n".format(__version__))
    print("This script installs/overwrites configs and style sheets for sway and nwg-shell components.")
    if not args.all:
        a = input("You will be prompted 'Y/n' at each step. Proceed? Y/n ")
        if a.strip().upper() != "Y":
            print("Installation cancelled")
            sys.exit(0)
    print("config_home = {}".format(config_home))
    paths = []
    bin_path = ""
    for path in os.getenv("PATH").split(":"):
        if path.startswith(os.getenv("HOME")) and os.path.exists(path):
            paths.append(path)
    if len(paths) == 1:
        bin_path = paths[0]
    else:
        for i in range(len(paths)):
            print("{}) {}".format(i + 1, paths[i]))

        while bin_path == "":
            i = input("Select folder to install scripts to: ")
            try:
                bin_path = paths[int(i) - 1]
            except:
                pass
        print("Installing scripts to {}".format(bin_path))


if __name__ == '__main__':
    main()
