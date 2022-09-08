#!/usr/bin/env bash

python3 setup.py install --optimize=1
cp nwg-shell.jpg /usr/share/backgrounds/
cp scripts/* /usr/local/bin/