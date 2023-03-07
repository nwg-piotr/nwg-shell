#!/usr/bin/python3

"""
This script checks the installed nwg-shell package version, first installed shell version, and performed updates,
recorded in the shell data file. If the shell needs an update, it sends a notification, and saves the lock file,
to avoid consecutive runs -> notifications in the same sway session. The lock file will be then removed in `autostart`.

Project: https://github.com/nwg-piotr/nwg-shell
Author's email: nwg.piotr@gmail.com
Copyright (c) 2022 Piotr Miller
License: MIT
"""
import os
import subprocess
import sys
import time

from nwg_shell.__about__ import __version__

from nwg_shell.tools import check_key, load_json, save_string, temp_dir, eprint

data_home = os.getenv('XDG_DATA_HOME') if os.getenv('XDG_DATA_HOME') else os.path.join(os.getenv("HOME"),
                                                                                       ".local/share")
tmp_dir = temp_dir()


def main():
    lock_file = os.path.join(tmp_dir, "nwg-shell-check-update.lock")
    if os.path.isfile(lock_file):
        # don't notify twice
        print("'{}' file found, terminating".format(lock_file))
        sys.exit(0)

    # This file will be removed in autostart
    save_string(str("this is to avoid multiple nwg-shell update checks in the same sway session"), lock_file)

    shell_data_file = os.path.join(data_home, "nwg-shell/data")

    if not os.path.isfile(shell_data_file):
        eprint("'{}' file not found, can't check updates. Terminating.".format(shell_data_file))
        sys.exit(1)

    shell_data = load_json(shell_data_file)
    if not shell_data:
        eprint("'{}' file corrupted, can't check updates. Terminating.".format(shell_data_file))
        sys.exit(1)

    # "installed-version" and "updates" keys will be missing from pre-0.3.0 installs
    # we only substitute them temporarily here, w/o saving
    defaults = {
        "installed-version": "0.0.0",
        "updates": [],
        "interface-locale": ""
    }
    for key in defaults:
        check_key(shell_data, key, defaults[key])

    # Shell versions that need to trigger update
    need_update = ["0.3.0", "0.3.4"]

    if __version__ > shell_data["installed-version"]:
        # If not just installed
        pending_updates = []
        for version in need_update:
            if version not in shell_data["updates"] and version > shell_data["installed-version"]:
                pending_updates.append(version)

        if len(pending_updates) > 0:
            updates_desc = ", ".join(pending_updates)
            print("Update(s) to {} available.".format(", ".join(pending_updates)))
            # notification looks better if appears after a period of time since startup
            time.sleep(5)
            # send notification with actions, wait for response
            output = subprocess.check_output(
                'exec {}'.format(
                    "notify-send -i /usr/share/pixmaps/nwg-shell.svg 'nwg-shell update' "
                    "'Update(s) to {} available!' --action=update=Update --action=later=Later --wait".format(
                        updates_desc)), shell=True)

            if output.strip().decode("utf-8") == "update":
                # run updater script
                subprocess.call('exec nwg-shell-updater', shell=True)
        else:
            print("No upgrade needed.")
    else:
        print("Just installed.")


if __name__ == '__main__':
    main()
