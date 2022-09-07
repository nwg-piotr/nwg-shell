#!/usr/bin/python3

import os
import subprocess
import sys
import time

from nwg_shell.__about__ import __version__

from nwg_shell.tools import load_json, save_string, temp_dir, eprint

data_home = os.getenv('XDG_DATA_HOME') if os.getenv('XDG_DATA_HOME') else os.path.join(os.getenv("HOME"),
                                                                                       ".local/share")
tmp_dir = temp_dir()


def main():
    lock_file = os.path.join(tmp_dir, "nwg-shell-check-update.lock")
    if os.path.isfile(lock_file):
        # Don't notify twice. The lock file will be removed in autostart.
        print("'{}' file found, terminating".format(lock_file))
        sys.exit(0)

    save_string(str(os.getpid()), lock_file)

    shell_data_file = os.path.join(data_home, "nwg-shell/data")

    if not os.path.isfile(shell_data_file):
        eprint("'{}' file not found, can't check updates. Terminating.".format(shell_data_file))
        sys.exit(1)

    shell_data = load_json(shell_data_file)
    if not shell_data:
        eprint("'{}' file corrupted, can't check updates. Terminating.".format(shell_data_file))
        sys.exit(1)

    # Shell versions that need to trigger upgrade
    need_update = ["0.3.0"]

    if __version__ > shell_data["installed-version"]:
        # If not just installed
        pending_updates = []
        for version in need_update:
            if version not in shell_data["updates"]:
                pending_updates.append(version)
        if len(pending_updates) > 0:
            updates_desc = ", ".join(pending_updates)
            print("Update(s) to {} available.".format(", ".join(pending_updates)))
            time.sleep(5)
            output = subprocess.check_output(
                'exec {}'.format(
                    "notify-send -i /usr/share/pixmaps/nwg-shell.svg 'nwg-shell update' "
                    "'Update(s) to {} available!' --action=update=Update --action=later=Later --wait".format(
                        updates_desc)), shell=True)
            print("'{}'".format(output.strip().decode("utf-8")))
            if output.strip().decode("utf-8") == "update":
                subprocess.call('exec nwg-shell-updater', shell=True)
        else:
            print("No upgrade needed.")
    else:
        print("Just installed.")


if __name__ == '__main__':
    main()
