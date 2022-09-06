#!/usr/bin/python3

"""
nwg-shell installer, to copy all the components' configs and style sheets to their locations,
or to restore original files. Pass the `--all` argument on first run, or none to select/restore files interactively.
Intended to work / tested with just-installed Arch Linux.
The package dependencies should pull all the packages needed for the nwg-shell to run.

Project: https://github.com/nwg-piotr/nwg-shell
Author's email: nwg.piotr@gmail.com
Copyright (c) 2022 Piotr Miller
License: MIT
"""

import argparse
import datetime
import os
import sys
from shutil import copy, copytree

from nwg_shell.__about__ import __version__

from nwg_shell.tools import load_json, save_json

dir_name = os.path.dirname(__file__)

config_home = os.getenv('XDG_CONFIG_HOME') if os.getenv('XDG_CONFIG_HOME') else os.path.join(os.getenv("HOME"),
                                                                                             ".config")

data_home = os.getenv('XDG_DATA_HOME') if os.getenv('XDG_DATA_HOME') else os.path.join(os.getenv("HOME"),
                                                                                       ".local/share")

shell_data = []
shell_data_file = os.path.join(data_home, "nwg-shell/data")


def copy_from_skel(name, folder="config", skip_confirmation=False):
    a = input("Install/overwrite files in the '{}' directory? y/N ".format(name)) if not skip_confirmation else "Y"
    if a.strip().upper() != "Y":
        print("'{}' directory skipped".format(name))
        return
    else:
        src = os.path.join(dir_name, "skel/{}/".format(folder), name)
        if folder == "data":
            dst = os.path.join(data_home, name)
        else:
            dst = os.path.join(config_home, name)
        print("Copying files to '{}'".format(dst), end=" ")
        try:
            copytree(src, dst, dirs_exist_ok=True)
            print("OK")
        except Exception as e:
            print("Failure: {}".format(e), file=sys.stderr)


def update_sway_config():
    # backup original file
    now = datetime.datetime.now()
    new_name = now.strftime("config-backup-%Y%m%d-%H%M%S")
    src = os.path.join(config_home, "sway/config")
    dst = os.path.join(config_home, "sway/{}".format(new_name))
    try:
        if os.path.isfile(src):
            copy(src, dst)
            print("Your old sway config file has been saved as '{}'".format(new_name))
    except Exception as e:
        print("Couldn't back up your old sway config: {}".format(e))

    a = input("You are about to overwrite your sway config file. Proceed? y/N ")
    proceed = a.strip().upper() == "Y"

    if proceed:
        src = os.path.join(dir_name, "skel/config/sway/config")
        dst = os.path.join(config_home, "sway/config")
        print("Copying '{}'".format(dst), end=" ")
        try:
            copy(src, dst)
            print("OK")
        except Exception as e:
            print(e)
    else:
        print("Sway config file update skipped.")


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

    # Load own data file, initiate first if it doesn't exist
    global shell_data
    if not os.path.isfile(shell_data_file):
        if not os.path.isdir(os.path.join(data_home, "nwg-shell")):
            os.makedirs(os.path.join(data_home, "nwg-shell"))
        shell_data = {"installed-version": __version__}
        save_json(shell_data, shell_data_file)
    else:
        shell_data = load_json(shell_data_file)
        # We no longer need the pre-v030 "last-upgrade" key
        if "last-upgrade" in shell_data:
            del shell_data["last-upgrade"]
            save_json(shell_data, shell_data_file)

    print("shell_data", shell_data)
    print("\n-------------------------------------------------------------------")
    print("|   This script installs/overwrites configs and style sheets      |")
    print("|             for sway and nwg-shell components.                  |")
    print("| The only backup that will be made is the main sway config file. |")
    print("|  This script should be used on a fresh Arch Linux installation. |")
    print("|         If you're running it on your existing sway setup,       |")
    print("|                you're doing it at your own risk.                |")
    print("-------------------------------------------------------------------")
    a = input("\nProceed? y/N ")
    if a.strip().upper() != "Y":
        print("Installation cancelled")
        sys.exit(0)

    # Backup sway config file
    now = datetime.datetime.now()
    new_name = now.strftime("config-backup-%Y%m%d-%H%M%S")
    src = os.path.join(config_home, "sway/config")
    dst = os.path.join(config_home, "sway/{}".format(new_name))
    proceed = True
    try:
        if os.path.isfile(src):
            copy(src, dst)
            print("* Original sway config file copied to '{}'".format(new_name))
    except Exception as e:
        print("Error: {}".format(e))
        a = input("Proceed with installation? y/N ")
        proceed = a.strip().upper() == "Y"

    if proceed:
        for item in ["sway", "nwg-panel", "nwg-wrapper", "nwg-drawer", "nwg-dock", "nwg-bar", "swaync", "foot"]:
            copy_from_skel(item, folder="config", skip_confirmation=args.all)
        for item in ["nwg-look"]:
            copy_from_skel(item, folder="data", skip_confirmation=args.all)

        print("\n\nThat's all. You may run sway now.\n")

        shell_data = {"last-upgrade": __version__}
        save_json(shell_data, shell_data_file)


if __name__ == '__main__':
    main()
