#!/usr/bin/python3

from nwg_shell.__about__ import __version__


def main():
    print("nwg-shell version {}".format(__version__))
    print("Commands:")
    print("  nwg-shell-installer      installs selected default configs interactively")
    print("  nwg-shell-installer -a   installs All configs from scratch")
    print("  nwg-shell-installer -r   Restore missing configs, styles & data files")
    print("  nwg-shell-check-updates  checks for updates")
    print('\nWiki: https://github.com/nwg-piotr/nwg-shell/wiki')


if __name__ == '__main__':
    main()
