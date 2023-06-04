#!/usr/bin/python3

"""
Installer script to copy all the components' configs and style sheets to their locations, or to restore original files.
Pass the `--all` argument to install/overwrite all, or use w/ no argument to restore selected files interactively.
This script is primarily intended to work (and tested!) on fresh installed Arch Linux.
See: https://github.com/nwg-piotr/nwg-shell/wiki

The package dependencies should pull all the packages needed for the nwg-shell to run.

Project: https://github.com/nwg-piotr/nwg-shell
Author's email: nwg.piotr@gmail.com
Copyright (c) 2022 Piotr Miller
License: MIT
"""

import argparse
import datetime
import os
import subprocess
import sys
from shutil import copy, copytree

from nwg_shell.__about__ import __version__

from nwg_shell.tools import load_json, save_json, is_command

dir_name = os.path.dirname(__file__)

config_home = os.getenv('XDG_CONFIG_HOME') if os.getenv('XDG_CONFIG_HOME') else os.path.join(os.getenv("HOME"),
                                                                                             ".config")

data_home = os.getenv('XDG_DATA_HOME') if os.getenv('XDG_DATA_HOME') else os.path.join(os.getenv("HOME"),
                                                                                       ".local/share")

shell_data = None
shell_data_file = os.path.join(data_home, "nwg-shell/data")

browsers = {
    "brave": "brave --enable-features=UseOzonePlatform --ozone-platform=wayland",
    "chromium": "chromium --enable-features=UseOzonePlatform --ozone-platform=wayland",
    "google-chrome-stable": "google-chrome-stable --enable-features=UseOzonePlatform --ozone-platform=wayland",
    "epiphany": "epiphany",
    "falkon": "falkon",
    "firefox": "MOZ_ENABLE_WAYLAND=1 firefox",
    "konqueror": "konqueror",
    "midori": "midori",
    "microsoft-edge-stable": "microsoft-edge-stable --enable-features=UseOzonePlatform --ozone-platform=wayland",
    "opera": "opera",
    "qutebrowser": "qutebrowser",
    "seamonkey": "seamonkey",
    "surf": "surf",
    "vivaldi-stable": "vivaldi-stable --enable-features=UseOzonePlatform --ozone-platform=wayland",
}


def copy_from_skel(name, folder="config", skip_confirmation=False):
    src = os.path.join(dir_name, "skel/{}/".format(folder), name)
    if folder == "data":
        dst = os.path.join(data_home, name)
    else:
        dst = os.path.join(config_home, name)

    a = input("Install/overwrite files in the '{}' directory? y/N ".format(dst)) if not skip_confirmation else "Y"
    if a.strip().upper() != "Y":
        print("'{}' directory skipped".format(dst))
        return

    else:
        print("Copying files to '{}'".format(dst), end=" ")
        try:
            copytree(src, dst, dirs_exist_ok=True)
            print("OK")
        except Exception as e:
            print("Failure: {}".format(e), file=sys.stderr)


def restore(name, folder="config"):
    src = os.path.join(dir_name, "skel/{}/".format(folder), name)
    if folder == "data":
        dst = os.path.join(data_home, name)
        if not os.path.isdir(dst):
            os.mkdir(dst)
    else:
        dst = os.path.join(config_home, name)
        if not os.path.isdir(dst):
            os.mkdir(dst)

    response = []

    for f in os.listdir(src):
        src_path = os.path.join(src, f)
        dst_path = os.path.join(dst, f)
        try:
            if not os.path.isfile(dst_path):
                copy(src_path, dst_path, follow_symlinks=False)
                response.append("Copied '{}'".format(dst_path))

        except Exception as e:
            response.append("Couldn't copy '{}' to '{}': {}".format(src_path, dst_path, e))

    return "\n".join(response) if len(response) > 0 else None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a",
                        "--all",
                        action="store_true",
                        help="install/overwrite All configs and styles w/o confirmation")
    parser.add_argument("-r",
                        "--restore",
                        action="store_true",
                        help="Restore missing configs, styles & data files")
    parser.add_argument("-w",
                        "--web",
                        action="store_true",
                        help="Web installer - skip confirmations")
    parser.add_argument("-v",
                        "--version",
                        action="version",
                        version="%(prog)s version {}".format(__version__),
                        help="display Version information")
    args = parser.parse_args()

    if args.restore:
        summary = []
        for item in ["sway", "nwg-panel", "nwg-drawer", "nwg-dock", "nwg-bar", "swaync", "foot", "gtklock"]:
            r = restore(item, folder="config")
            if r:
                summary.append(r)
        for item in ["nwg-look"]:
            r = restore(item, folder="data")
            if r:
                summary.append(r)
        if len(summary) > 0:
            print("\n".join(summary))

        sys.exit(0)

    global shell_data

    if not args.web:
        print("\n*******************************************************************")
        print("    This script installs/overwrites configs and style sheets       ")
        print("          for sway, Hyprland and nwg-shell components.             ")
        print("  The only backup that will be made is the main sway config file.  ")
        print("   This script should be used on a fresh Arch Linux installation.  ")
        print("            If you're running it on your existing setup,           ")
        print("                 you're doing it at your own risk.                 ")
        print("*******************************************************************")

        a = input("\nProceed? y/N ")
    else:
        a = "Y"

    if a.strip().upper() != "Y":
        print("Installation cancelled")
        sys.exit(0)
    else:
        if not os.path.isfile(shell_data_file):
            # It must be a new installation. We need to init and save the shell data file.
            if not os.path.isdir(os.path.join(data_home, "nwg-shell")):
                os.makedirs(os.path.join(data_home, "nwg-shell"))
            shell_data = {
                "installed-version": __version__,
                "updates": [__version__],
                "interface-locale": ""
            }
            save_json(shell_data, shell_data_file)

        else:
            # Installing over existing install
            shell_data = load_json(shell_data_file)
            # We no longer need the pre-v0.3.0 "last-upgrade" key: delete it if found
            if "last-upgrade" in shell_data:
                del shell_data["last-upgrade"]
                save_json(shell_data, shell_data_file)

    # Backup sway config file (we may have none on fresh installation)
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
        skip = args.all or args.web
        for item in ["sway", "nwg-panel", "nwg-drawer", "nwg-dock", "nwg-bar", "nwg-look", "swaync", "foot", "gtklock"]:
            copy_from_skel(item, folder="config", skip_confirmation=skip)
        for item in ["nwg-look", "nwg-shell-config"]:
            copy_from_skel(item, folder="data", skip_confirmation=skip)

        # Set default apps, if found, for nwg-shell-config
        shell_config_settings_file = os.path.join(data_home, "nwg-shell-config", "settings")
        shell_config_settings = load_json(shell_config_settings_file)

        if "terminal" not in shell_config_settings or not shell_config_settings["terminal"]:
            shell_config_settings["terminal"] = "foot"

        if "file-manager" not in shell_config_settings or not shell_config_settings["file-manager"]:
            for cmd in ["thunar", "caja", "dolphin", "nautilus", "nemo", "pcmanfm"]:
                if is_command(cmd):
                    shell_config_settings["file-manager"] = cmd
                    break

        if "editor" not in shell_config_settings or not shell_config_settings["editor"]:
            for cmd in ["mousepad", "atom", "emacs", "gedit", "geany", "kate", "vim"]:
                if is_command(cmd):
                    shell_config_settings["editor"] = cmd
                    break

        if "browser" not in shell_config_settings or not shell_config_settings["browser"]:
            for cmd in ["brave", "chromium", "google-chrome-stable", "epiphany", "falkon", "firefox", "konqueror",
                        "midori", "microsoft-edge-stable", "opera", "qutebrowser", "seamonkey", "surf", "vivaldi-stable"]:
                if is_command(cmd):
                    shell_config_settings["browser"] = browsers[cmd]
                    break

        save_json(shell_config_settings, shell_config_settings_file)

        # Copy default background
        bcg = os.path.join(os.getenv("HOME"), "azotebg")
        if not os.path.isfile(bcg):
            print("Copying default background")
            copy(os.path.join(dir_name, "skel", "stuff", "azotebg"), bcg)
            os.rename(bcg, os.path.join(os.getenv("HOME"), ".azotebg"))

        if not args.web:
            print("\nThat's all. You may run sway now.\n")
        else:
            print("\nThat's all. For the brightness control to work, you need to reboot before running sway.\n")
            a = input("\nReboot now? Y/n ")
            if a.strip().upper() == "Y" or not a:
                subprocess.call("sudo reboot", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


if __name__ == '__main__':
    main()
