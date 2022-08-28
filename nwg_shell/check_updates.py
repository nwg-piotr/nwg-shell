#!/usr/bin/python3

import os
import subprocess
import time

from nwg_shell.__about__ import __version__

from nwg_shell.tools import load_json, save_json, is_newer

data_home = os.getenv('XDG_DATA_HOME') if os.getenv('XDG_DATA_HOME') else os.path.join(os.getenv("HOME"),
                                                                                       ".local/share")


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
    need_upgrade = ["0.2.0", "0.2.4"]

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
