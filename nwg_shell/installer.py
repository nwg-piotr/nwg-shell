#!/usr/bin/python3

"""
nwg-shell installer, to copy all the components' configs and style sheets to their locations,
or to restore original files. Pass the `--all` argument on first run or none to select files interactively.
Interned to work/tested with Arch Linux.
The package dependencies should pull all the packages needed for the nwg-shell to run.

Project: https://github.com/nwg-piotr/nwg-shell
Author's email: nwg.piotr@gmail.com
Copyright (c) 2022 Piotr Miller
License: MIT
"""

import os
import sys
import argparse
from shutil import copy, copy2, copytree
import datetime

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
        print("Copying files to '{}'".format(dst), end=" ")
        try:
            # copytree(src, dst, dirs_exist_ok=True)
            print("OK")
        except Exception as e:
            print("Failure: {}".format(e), file=sys.stderr)


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

    print("_______________________________________________________________________________________________")
    print("  This script installs/overwrites configs and style sheets for sway and nwg-shell components.  ")
    print("              The only backup that will be made is the main sway config file.                  ")
    print("  If you're running the script on your existing sway setup, you're doing it at your own risk.  ")
    print("_______________________________________________________________________________________________")
    a = input("\nProceed? Y/n ")
    if a.strip().upper() != "Y":
        print("Installation cancelled")
        sys.exit(0)

    a = input("Install helper scripts? Y/n ") if not args.all else "Y"
    if a.strip().upper() == "Y" or args.all:
        print("\n[Scripts installation]")
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
            print("Copying {}".format(os.path.join(bin_path, file)), end=" ")
            try:
                copy2(os.path.join(src, file), os.path.join(bin_path, file))
                print("OK")
            except Exception as e:
                print("Failure: {}".format(e), file=sys.stderr)

        src = os.path.join(dir_name, "skel/azotebg")
        dst = os.path.join(os.getenv("HOME"), ".azotebg")
        print("Copying {}".format(dst), end=" ")
        try:
            copy2(src, dst)
            print("OK")
        except Exception as e:
            print("Failure: {}".format(e), file=sys.stderr)

    a = input("Install configs and style sheets? Y/n ") if not args.all else "Y"
    if a.strip().upper() == "Y" or args.all:
        print("\n[Configs installation]")

        # Backup sway config file
        now = datetime.datetime.now()
        new_name = now.strftime("config-backup-%Y%m%d-%H%M%S")
        src = os.path.join(config_home, "sway/config")
        dst = os.path.join(config_home, "sway/{}".format(new_name))
        proceed = True
        backup = False
        try:
            copy(src, dst)
            backup = True
        except Exception as e:
            print("Error: {}".format(e))
            a = input("Proceed with installation? Y/n ")
            proceed = a.strip().upper() == "Y"

        if proceed:
            for item in ["gtk-3.0", "sway", "nwg-panel", "nwg-wrapper", "nwg-drawer", "nwg-dock", "nwg-bar", "swaync"]:
                copy_from_skel(item, args.all)
            if backup:
                print("\n*** Original sway config file '{}' has been renamed to '{}'".format(src, new_name))
            print("That's all. You may run sway now.")
        else:
            print("Configs installation cancelled")


if __name__ == '__main__':
    main()
