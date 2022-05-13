#!/usr/bin/python3

from nwg_shell.__about__ import __version__


def main():
    print("nwg-shell version {}".format(__version__))
    print("Commands:")
    print("  nwg-shell-installer      installs selected default configs interactively")
    print("  nwg-shell-installer -a   installs all configs from scratch")
    print("  nwg-shell-installer -u   upgrades configs if necessary")
    print("  nwg-shell-check-updates  checks for updates")


if __name__ == '__main__':
    main()
