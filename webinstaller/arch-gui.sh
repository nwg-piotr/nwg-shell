#!/usr/bin/bash

sudo pacman -S --noconfirm git man-db vi xdg-user-dirs
# Set up user dirs
xdg-user-dirs-update
# Let `light` | `brightnessctl` work (needs restart)
sudo usermod -aG video $USER

# Set up Basic AUR Package Helper
git clone https://bitbucket.org/natemaia/baph.git
cd baph || { echo "Failed cloning baph, terminating"; exit 1; }
sudo make install

# Copy & modify default sway config file
mkdir -p ~/.config/sway
cp /etc/sway/config ~/.config/sway
echo 'exec nwg-shell-installer-gui' >> ~/.config/sway/config

baph -inN nwg-shell
nwg-shell-installer -w
