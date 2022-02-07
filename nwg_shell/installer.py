#!/usr/bin/python3

"""
This is going to work as the nwg-shell installer, but also as the shell meta-package.
The script is very basic, and will need need some improvement.
"""

import os
import sys
import argparse
from shutil import copy2, copytree

from nwg_shell.__about__ import __version__

dir_name = os.path.dirname(__file__)

config_home = os.getenv('XDG_CONFIG_HOME') if os.getenv('XDG_CONFIG_HOME') else os.path.join(os.getenv("HOME"),
                                                                                             ".config")


def copy_from_skel(name, skip_confirmation=False):
    a = input("Install/overwrite files in the '{}' directory? Y/n ".format(name)) if not skip_confirmation else "Y"
    if a.strip().upper() != "Y":
        print("'{}' directory skipped".format(name))
        return
    else:
        src = os.path.join(dir_name, "skel/config/", name)
        dst = os.path.join(config_home, name)
        print("Copying files to '{}'".format(dst))
        copytree(src, dst, dirs_exist_ok=True)


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

    print("This script installs/overwrites configs and style sheets for sway and nwg-shell components.")
    if not args.all:
        a = input("You will be prompted 'Y/n' at each step. Proceed? Y/n ")
        if a.strip().upper() != "Y":
            print("Installation cancelled")
            sys.exit(0)

    a = input("Install helper scripts? Y/n ") if not args.all else "Y"
    if a.strip().upper() == "Y" or args.all:
        print("[Scripts installation]")
        paths = []
        bin_path = ""
        for path in os.getenv("PATH").split(":"):
            if path.startswith(os.getenv("HOME")) and os.path.exists(path):
                paths.append(path)
        if len(paths) == 0:
            print("No directory in '{}' found on $PATH, dunno where to install scripts, sorry".format(os.getenv("HOME")))
            sys.exit(1)
        elif len(paths) == 1 or args.all:
            bin_path = paths[0]
        else:
            print("More then 1 possible path for scripts found:")
            for i in range(len(paths)):
                print("  {}) {}".format(i + 1, paths[i]))

            while bin_path == "":
                i = input("Select folder to install scripts to: ")
                try:
                    bin_path = paths[int(i) - 1]
                except:
                    pass

        src = os.path.join(dir_name, "skel/bin/")
        for file in os.listdir(src):
            print("Copying {}".format(os.path.join(bin_path, file)))
            copy2(os.path.join(src, file), os.path.join(bin_path, file))

    print("[Configs installation]")
    for item in ["sway", "nwg-panel", "nwg-wrapper", "nwg-drawer", "nwg-dock", "nwg-bar", "swaync"]:
        copy_from_skel(item, args.all)


if __name__ == '__main__':
    main()
