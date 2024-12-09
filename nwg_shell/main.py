#!/usr/bin/python3

from nwg_shell.__about__ import __version__


def main():
    print("nwg-shell version {}".format(__version__))
    print("Commands:")
    print("  nwg-shell-installer            installs selected default configs interactively")
    print("  nwg-shell-installer -a [-hypr] installs All configs from scratch; [-hypr] includes Hyprland configs")
    print("  nwg-shell-installer -w [-hypr] installs configs from scratch w/ no dialogs; [-hypr] includes Hyprland configs")
    print("  nwg-shell-installer -r [-hypr] Restores missing configs, styles & data files; [-hypr] includes Hyprland configs")
    print('\nWiki: https://github.com/nwg-piotr/nwg-shell/wiki')


if __name__ == '__main__':
    main()
