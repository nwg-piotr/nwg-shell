#!/usr/bin/env bash

python3 setup.py install --optimize=1

install -Dm 644 -t "/usr/share/licenses/nwg-shell" LICENSE
install -Dm 644 -t "/usr/share/doc/nwg-shell" README.md
install -Dm 644 -t "/usr/share/applications" nwg-readme.desktop
