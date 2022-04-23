#!/usr/bin/python3

from nwg_shell.__about__ import __version__


def main():
    print("nwg-shell version {}".format(__version__))
    print("Run `nwg-shell-installer -a` to install all components from scratch or `nwg-shell-installer` to install"
          "/overwrite selected components in interactive mode.")
    print("Run `nwg-shell-installer -u` to upgrade nwg-shell to the {} version.".format(__version__))


if __name__ == '__main__':
    main()
