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
import json
import subprocess
from shutil import copy, copy2, copytree
import datetime

from nwg_shell.__about__ import __version__

dir_name = os.path.dirname(__file__)

config_home = os.getenv('XDG_CONFIG_HOME') if os.getenv('XDG_CONFIG_HOME') else os.path.join(os.getenv("HOME"),
                                                                                             ".config")


def load_json(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print("Error loading json: {}".format(e))
        return None


def save_json(src_dict, path):
    with open(path, 'w') as f:
        json.dump(src_dict, f, indent=2)


def is_command(cmd):
    cmd = cmd.split()[0]  # strip arguments
    cmd = "command -v {}".format(cmd)
    try:
        is_cmd = subprocess.check_output(cmd, shell=True).decode("utf-8").strip()
        if is_cmd:
            return is_cmd

    except subprocess.CalledProcessError:
        return ""


def launch(cmd):
    print("Executing '{}'".format(cmd))
    subprocess.Popen('exec {}'.format(cmd), shell=True)


def copy_from_skel(name, skip_confirmation=False):
    a = input("Install/overwrite files in the '{}' directory? y/n ".format(name)) if not skip_confirmation else "Y"
    if a.strip().upper() != "Y":
        print("'{}' directory skipped".format(name))
        return
    else:
        src = os.path.join(dir_name, "skel/config/", name)
        dst = os.path.join(config_home, name)
        print("Copying files to '{}'".format(dst), end=" ")
        try:
            copytree(src, dst, dirs_exist_ok=True)
            print("OK")
        except Exception as e:
            print("Failure: {}".format(e), file=sys.stderr)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a",
                        "--all",
                        action="store_true",
                        help="Install/overwrite all configs and styles w/o confirmation")
    parser.add_argument("-u",
                        "--upgrade",
                        action="store_true",
                        help="Upgrade current nwg-shell install")
    parser.add_argument("-v",
                        "--version",
                        action="version",
                        version="%(prog)s version {}".format(__version__),
                        help="display version information")
    args = parser.parse_args()

    if args.upgrade:
        print("You are about to upgrade nwg-shell to v{}.".format(__version__))
        print("This will modify your config files to use the recently added software.")
        a = input("\nProceed? y/n ")
        if a.strip().upper() != "Y":
            print("Installation cancelled")
            sys.exit(0)
        else:
            for item in ["preset-0", "preset-1", "preset-2", "preset-3"]:
                src = os.path.join(config_home, "nwg-panel/{}".format(item))
                panel_config = load_json(src)
                for panel in panel_config:
                    if "custom-items" in panel["controls-settings"]:
                        for i in panel["controls-settings"]["custom-items"]:
                            # replace lxappearance with nwg-look
                            if "lxappearance" in i["cmd"]:
                                print("replacing 'lxappearance' with 'nwg-look' in '{}'".format(item))
                                i["name"] = "GTK settings"
                                i["icon"] = "nwg-look"
                                i["cmd"] = "nwg-look"

                            if "wdisplays" in i["cmd"]:
                                print("replacing 'wdisplays' with 'nwg-displays' in '{}'".format(item))
                                i["name"] = "Displays"
                                i["icon"] = "nwg-displays"
                                i["cmd"] = "nwg-displays"

        launch("swaymsg reload")

    else:
        print("-------------------------------------------------------------------")
        print("|   This script installs/overwrites configs and style sheets      |")
        print("|             for sway and nwg-shell components.                  |")
        print("| The only backup that will be made is the main sway config file. |")
        print("|  This script should be used on a fresh Arch Linux installation. |")
        print("|         If you're running it on your existing sway setup,       |")
        print("|                you're doing it at your own risk.                |")
        print("|                                                                 |")
        print("|          See 'nwg-shell-installer -h' for other options.        |")
        print("-------------------------------------------------------------------")
        a = input("\nProceed? y/n ")
        if a.strip().upper() != "Y":
            print("Installation cancelled")
            sys.exit(0)

        a = input("Install helper scripts? Y/n ") if not args.all else "Y"
        if a.strip().upper() == "Y" or args.all:
            print("\n[Scripts installation]")
            paths = []
            bin_path = ""
            for path in os.getenv("PATH").split(":"):
                if path.startswith(os.getenv("HOME")) and os.path.exists(path) and path not in paths:
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

        a = input("Install configs and style sheets? y/n ") if not args.all else "Y"
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
                if os.path.isfile(src):
                    copy(src, dst)
                    backup = True
            except Exception as e:
                print("Error: {}".format(e))
                a = input("Proceed with installation? y/n ")
                proceed = a.strip().upper() == "Y"

            if proceed:
                for item in ["gtk-3.0", "sway", "nwg-panel", "nwg-wrapper", "nwg-drawer", "nwg-dock", "nwg-bar",
                             "swaync"]:
                    copy_from_skel(item, args.all)
                if backup:
                    print("\n*** Original sway config file '{}' has been renamed to '{}'".format(src, new_name))
                print("That's all. You may run sway now.")
            else:
                print("Configs installation cancelled")

    # Inform about no longer needed stuff
    # Packages
    for item in ["lxappearance", "wdisplays"]:
        if is_command(item):
            print("The '{}' package is no longer necessary, you may uninstall it now.".format(item))

    # Scripts
    for item in ["import-gsettings", "sway-save-outputs"]:
        if is_command(item):
            c = is_command(item)
            if c:
                print("The '{}' script is no longer necessary, you may delete it now.".format(c))


if __name__ == '__main__':
    main()
