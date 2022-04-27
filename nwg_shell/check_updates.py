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


def ver2int(ver):
    """
    Simple conversion for Semantic Versioning 2.0 string to integer, e.g. '0.2.1' to 21
    Valid for numbers 0-9 only!
    :param ver: str
    :return: int
    """
    try:
        nums = ver.split(".")
        if len(nums) != 3:
            return None
        return int(nums[0]) * 100 + int(nums[1]) * 10 + int(nums[2])
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

    last_upgrade = ver2int(shell_data["last-upgrade"])
    ver = ver2int(__version__)

    if last_upgrade is not None and ver is not None:
        if last_upgrade < ver and __version__ in need_upgrade:
            time.sleep(3)
            subprocess.Popen(
                'exec {}'.format("notify-send -i /usr/share/pixmaps/nwg-shell.svg 'Upgrade to nwg-shell v{} "
                                 "available' 'Run \"nwg-shell-installer -u\" in terminal.'".format(__version__)),
                shell=True)
            print("Upgrade to {} needed. Run 'nwg-shell-installer -u'.".format(__version__))
        else:
            print("No upgrade needed.")
    else:
        print("Couldn't check if upgrade needed.")


if __name__ == '__main__':
    main()
