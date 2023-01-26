#!/usr/bash
sudo pacman -s chromium mousepad thunar nano git man-db vi xdg-user-dirs
xdg-user-dirs-update
sudo usermod -aG video $USER
mkdir ~/Clones
cd ~/Clones
git clone https://bitbucket.org/natemaia/baph.git
cd baph
sudo make install
baph -inN nwg-shell
nwg-shell-installer -a
echo You may need to reboot for the brightness controll to work!
