#!/usr/bin/python3

"""
nwg-shell installer, to copy all the components' configs and style sheets to their locations,
or to restore original files. Pass the `--all` argument on first run or none to select files interactively.
Intended to work/tested with Arch Linux.
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
from shutil import copy, copy2, copytree

from nwg_shell.__about__ import __version__

from nwg_shell.tools import load_json, save_json, load_text_file, save_list_to_text_file

dir_name = os.path.dirname(__file__)

config_home = os.getenv('XDG_CONFIG_HOME') if os.getenv('XDG_CONFIG_HOME') else os.path.join(os.getenv("HOME"),
                                                                                             ".config")

data_home = os.getenv('XDG_DATA_HOME') if os.getenv('XDG_DATA_HOME') else os.path.join(os.getenv("HOME"),
                                                                                       ".local/share")

shell_data = []
shell_data_file = os.path.join(data_home, "nwg-shell/data")


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

    # Load own data file, initiate first if it doesn't exist
    if not os.path.isdir(os.path.join(data_home, "nwg-shell/")):
        copy_from_skel("nwg-shell", folder="data", skip_confirmation=True)
    global shell_data
    if not os.path.isfile(shell_data_file):
        if not os.path.isdir(os.path.join(data_home, "nwg-shell")):
            os.makedirs(os.path.join(data_home, "nwg-shell"))
        shell_data = {"last-upgrade": __version__}
        save_json(shell_data, shell_data_file)
    else:
        shell_data = load_json(shell_data_file)

    # Upgrade
    if args.upgrade:
        print("--------------------------------------------------------------")
        print("|       You are about to upgrade nwg-shell to v{}.        |".format(__version__))
        print("|    This will modify and/or replace your config files.      |")
        print("|                                                            |")
        print("|   If something goes wrong, run 'nwg-shell-installer -a'    |")
        print("|        or 'nwg-shell-installer' (interactive mode),        |")
        print("|            in order to install default configs.            |")
        print("--------------------------------------------------------------")

        a = input("\nProceed? y/N ")
        if a.strip().upper() != "Y":
            print("Installation cancelled")
            sys.exit(0)
        else:
            if __version__ == "0.2.0":
                print("\n[Updating panel presets]")
                for item in ["preset-0", "preset-1", "preset-2", "preset-3"]:
                    src = os.path.join(config_home, "nwg-panel/{}".format(item))
                    panel_config = load_json(src)
                    changed = False
                    for panel in panel_config:
                        if "custom-items" in panel["controls-settings"]:
                            for i in panel["controls-settings"]["custom-items"]:
                                # replace lxappearance with nwg-look
                                if "lxappearance" in i["cmd"]:
                                    print("replacing 'lxappearance' with 'nwg-look' in '{}'".format(item))
                                    i["name"] = "GTK settings"
                                    i["icon"] = "nwg-look"
                                    i["cmd"] = "nwg-look"
                                    changed = True

                                # replace wdisplays with nwg-displays
                                if "wdisplays" in i["cmd"]:
                                    print("replacing 'wdisplays' with 'nwg-displays' in '{}'".format(item))
                                    i["name"] = "Displays"
                                    i["icon"] = "nwg-displays"
                                    i["cmd"] = "nwg-displays"
                                    changed = True

                                # update nwg-shell-config
                                if "nwg-shell-config" in i["cmd"] and i["icon"] != "nwg-shell-config":
                                    print("updating 'nwg-shell-config' in '{}'".format(item))
                                    i["icon"] = "nwg-shell-config"
                                    changed = True

                    if changed:
                        print("Saving '{}'".format(src))
                        save_json(panel_config, src)

                if not changed:
                    print("No change needed.")

                update_sway_config()

                # Use nwg-look to apply default GTK settings if it has not been done yet
                if not os.path.isfile(os.path.join(data_home, "nwg-look/gsettings")):
                    print("\nApplying default GTK settings. Run 'nwg-look' utility to set your preferences.")
                    print("You'll find it in the 'Controls' menu as 'GTK settings'.")
                    copy_from_skel("nwg-look", folder="data", skip_confirmation=True)
                    launch("nwg-look -a")

            elif __version__ == "0.2.4":
                print("--------------------------------------------------------------")
                print("|  nwg-shell 0.2.4 simplifies some key bindings in the main  |")
                print("|   sway config file, and adds 2 buttons to panel presets.   |")
                print("| Also some minor bugs in related css files have been fixed. |")
                print("|   If you proceed with the upgrade, your sway config file,  |")
                print("|      panel presets and panel css style sheets will be      |")
                print("|              overwritten with new defaults.                |")
                print("|    Changes you made to panel presets 0-3 will be lost.     |")
                print("|        Your old sway config file will be backed up.        |")
                print("|                                                            |")
                print("|   You may also do it later with the `nwg-shell-installer`  |")
                print("|           or `nwg-shell-installer -a` command.             |")
                print("--------------------------------------------------------------\n")

                update_sway_config()

                a = input("\nOverwrite nwg-panel config files? y/N ")
                proceed = a.strip().upper() == "Y"

                if proceed:
                    copy_from_skel("nwg-panel", folder="config", skip_confirmation=True)
                else:
                    print("nwg-panel configs update cancelled.")

            elif __version__ == "0.2.5":
                print("--------------------------------------------------------------")
                print("|   nwg-shell 0.2.5 comes with own `nwg-autotiling` script,  |")
                print("|  that replaces the `autotiling` package. This is to avoid  |")
                print("| adding the nwg-shell-specific stuff to the original script,|")
                print("|       which is quite widely used outside the project.      |")
                print("|                                                            |")
                print("|   The `nwg-autotiling` script should be more stable here.  |")
                print("|                                                            |")
                print("|     The upgrade process will only replace `autotiling`     |")
                print("|   with `nwg-autotiling` in your `autostart` config file.   |")
                print("|                   It should be 100% safe.                  |")
                print("--------------------------------------------------------------\n")

                a = input("Proceed with `autostart` upgrade? y/N ")
                proceed = a.strip().upper() == "Y"

                if proceed:
                    autostart = os.path.join(config_home, "sway", "autostart")
                    old = load_text_file(autostart).splitlines()
                    new = []
                    changed = False
                    for line in old:
                        if "autotiling" not in line:
                            new.append(line)
                        else:
                            new.append("exec_always nwg-autotiling")
                            print("`autotiling` replaced  with nwg-autotiling")
                            changed = True

                    if changed:
                        save_list_to_text_file(new, autostart)
                    else:
                        print("No change needed")

        print("\n--------------------------------------------------------------")
        print("|             Restart sway for changes to take effect.       |")
        print("--------------------------------------------------------------\n")

        # Inform about no longer needed stuff
        # Packages
        for item in ["lxappearance", "wdisplays", "nwg-wrapper", "autotiling"]:
            if is_command(item):
                print("The '{}' package is no longer necessary, you may uninstall it now.".format(item))

        # Scripts
        for item in ["import-gsettings", "sway-save-outputs"]:
            if is_command(item):
                c = is_command(item)
                if c:
                    print("The '{}' script is no longer necessary, you may delete it now.".format(c))

        # Save shell data file
        shell_data = {"last-upgrade": __version__}
        save_json(shell_data, shell_data_file)

    # Installation
    else:
        print("\n-------------------------------------------------------------------")
        print("|   This script installs/overwrites configs and style sheets      |")
        print("|             for sway and nwg-shell components.                  |")
        print("| The only backup that will be made is the main sway config file. |")
        print("|  This script should be used on a fresh Arch Linux installation. |")
        print("|         If you're running it on your existing sway setup,       |")
        print("|                you're doing it at your own risk.                |")
        print("|                                                                 |")
        print("|          See 'nwg-shell-installer -h' for other options.        |")
        print("-------------------------------------------------------------------")
        a = input("\nProceed? y/N ")
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
                print("No directory in '{}' found on $PATH, dunno where to install scripts, sorry".format(
                    os.getenv("HOME")))
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

        a = input("Install configs, style sheets and initial data files? y/N ") if not args.all else "Y"
        if a.strip().upper() == "Y" or args.all:
            print("\n[Configs, styles and data installation]")

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
                for item in ["sway", "nwg-panel", "nwg-wrapper", "nwg-drawer", "nwg-dock", "nwg-bar", "swaync"]:
                    copy_from_skel(item, folder="config", skip_confirmation=args.all)
                for item in ["nwg-look"]:
                    copy_from_skel(item, folder="data", skip_confirmation=args.all)

                print("\n\nThat's all. You may run sway now.\n")

                shell_data = {"last-upgrade": __version__}
                save_json(shell_data, shell_data_file)
            else:
                print("File installation cancelled")


if __name__ == '__main__':
    main()
