#!/usr/bin/python3

import argparse
import json
import os
import subprocess

from nwg_shell.__about__ import __version__

data_home = os.getenv('XDG_DATA_HOME') if os.getenv('XDG_DATA_HOME') else os.path.join(os.getenv("HOME"),
                                                                                       ".local/share")

shell_data = []
shell_data_file = os.path.join(data_home, "nwg-shell/data")


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
    # Converts version to int, e.g. '0.2.1' to 21
    try:
        nums = ver.split(".")
        if len(nums) != 3:
            return None
        return int(nums[0]) * 100 + int(nums[1]) * 10 + int(nums[2])
    except:
        return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n",
                        "--notify",
                        action="store_true",
                        help="Send update notification if needed")

    args = parser.parse_args()

    if not args.notify:
        print("nwg-shell version {}".format(__version__))
        print("Run `nwg-shell-installer -a` to install all components from scratch or `nwg-shell-installer` to install"
              "/overwrite selected components in interactive mode.")
        print("\nRun `nwg-shell-installer -u` to upgrade components to the {} version.".format(__version__))
    else:
        # This is for use w/ 'nwg-shell-check-updates' command (a part of nwg-shell-config).
        # Will only be called if 'nwg-shell' package installed.
        global shell_data
        shell_data = load_json(shell_data_file)
        if not shell_data:
            if not os.path.isdir(os.path.join(data_home, "nwg-shell/")):
                os.makedirs(os.path.join(data_home, "nwg-shell"))

            shell_data = {"last-upgrade": "0.0.0"}
            save_json(shell_data, shell_data_file)

        # Installer versions that need to trigger upgrade
        need_upgrade = ["0.2.0"]
        if ver2int(shell_data["last-upgrade"]) < ver2int(__version__) and __version__ in need_upgrade:
            subprocess.Popen(
                'exec {}'.format("notify-send 'Upgrade to nwg-shell v{} available' "
                                 "'Run \"nwg-shell-installer -u\" in terminal.'".format(__version__)), shell=True)


if __name__ == '__main__':
    main()
