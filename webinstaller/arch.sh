#!/usr/bash

sudo pacman -S -noconfirm chromium mousepad thunar nano git man-db vi xdg-user-dirs
xdg-user-dirs-update
sudo usermod -aG video $USER
git clone https://bitbucket.org/natemaia/baph.git
cd baph || { echo "Failed cloning baph, terminating"; exit 1; }
sudo make install
baph -inN nwg-shell-git
nwg-shell-installer -w
