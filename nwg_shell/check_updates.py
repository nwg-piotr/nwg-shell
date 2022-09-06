#!/usr/bin/python3

import os
import subprocess
import sys
import time

from nwg_shell.__about__ import __version__

from nwg_shell.tools import load_json, save_string, temp_dir, launch, eprint

data_home = os.getenv('XDG_DATA_HOME') if os.getenv('XDG_DATA_HOME') else os.path.join(os.getenv("HOME"),
                                                                                       ".local/share")
tmp_dir = temp_dir()


def main():
    # If file present, we won't notify again
    notification_file = os.path.join(tmp_dir, "nwg-shell-update-notification")
    if os.path.isfile(notification_file):
        print("notification already sent, terminating")
        sys.exit(0)

    lock_file = os.path.join(tmp_dir, "nwg-shell-check-update.lock")
    if os.path.isfile(lock_file):
        # We are still waiting for user's response to the notification
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
    need_update = ["0.2.5", "0.3.0"]

    if __version__ > shell_data["installed-version"]:
        # If not just installed
        pending_updates = []
        for version in need_update:
            if version not in shell_data["updates"]:
                pending_updates.append(version)
        if len(pending_updates) > 0:
            updates_desc = ", ".join(pending_updates)
            print("Update(s) to {} available. Run 'nwg-shell-installer -u'.".format(", ".join(pending_updates)))
            time.sleep(5)
            save_string(updates_desc, notification_file)
            output = subprocess.check_output(
                'exec {}'.format(
                    "notify-send -i /usr/share/pixmaps/nwg-shell.svg 'nwg-shell update' "
                    "'Update(s) to {} available!' --action=update=Update --action=later=Later --wait".format(
                        updates_desc)), shell=True)
            print("'{}'".format(output.strip().decode("utf-8")))
            os.remove(lock_file)
            if output.strip().decode("utf-8") == "update":
                launch("nwg-shell-updater")
        else:
            print("No upgrade needed.")
    else:
        print("Just installed.")


if __name__ == '__main__':
    main()
