#!/usr/bin/bash

wget https://raw.github.com/nwg-piotr/nwg-shell/gui/webinstaller/test.sh -O test.sh;
chmod u+x test.sh
./test.sh &
rm test.sh
