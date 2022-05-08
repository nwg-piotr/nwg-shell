#!/usr/bin/python3

import json
import os
import subprocess
import time

from nwg_shell.__about__ import __version__

data_home = os.getenv('XDG_DATA_HOME') if os.getenv('XDG_DATA_HOME') else os.path.join(os.getenv("HOME"),
                                                                                       ".local/share")


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


def is_newer(string_new, string_existing):
    """
    Compares versions in format 'major.minor.patch' (just numbers allowed).
    :param string_new: new version to compare with existing one
    :param string_existing: existing version
    :return: True if new is newer then existing
    """
    new = major_minor_path(string_new)
    existing = major_minor_path(string_existing)
    if new and existing:
        if new[0] > existing[0]:
            return True
        elif new[1] > existing[1]:
            return True
        elif new[2] > existing[2]:
            return True
        else:
            return False
    else:
        return False


def major_minor_path(string):
    parts = string.split(".")
    if len(parts) != 3:
        return None
    try:
        return int(parts[0]), int(parts[1]), int(parts[2])
    except:
        return None


def main():
    shell_data_file = os.path.join(data_home, "nwg-shell/data")

    shell_data = load_json(shell_data_file)
    if not shell_data:
        if not os.path.isdir(os.path.join(data_home, "nwg-shell/")):
            os.makedirs(os.path.join(data_home, "nwg-shell"))

        print("Shell data file not found, creating default.")
        shell_data = {"last-upgrade": "0.0.0"}
        save_json(shell_data, shell_data_file)

    # Shell versions that need to trigger upgrade
    need_upgrade = ["0.2.0"]

    # last_upgrade = ver2int(shell_data["last-upgrade"])
    # ver = ver2int(__version__)

    if shell_data["last-upgrade"] and __version__:
        if is_newer(__version__, shell_data["last-upgrade"]) and __version__ in need_upgrade:
            print("Upgrade to {} needed. Run 'nwg-shell-installer -u'.".format(__version__))
            time.sleep(5)
            subprocess.Popen(
                'exec {}'.format("notify-send -i /usr/share/pixmaps/nwg-shell.svg 'nwg-shell v{} available' "
                                 "'Run \"nwg-shell-installer -u\" in terminal.'".format(__version__)), shell=True)
        else:
            print("No upgrade needed.")
    else:
        print("Couldn't check if upgrade needed.")


if __name__ == '__main__':
    main()
