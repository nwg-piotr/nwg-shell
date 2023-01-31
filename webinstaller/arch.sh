#!/usr/bin/bash

sudo pacman -S --noconfirm git man-db vi xdg-user-dirs
# Set up user dirs
xdg-user-dirs-update
# Let `light` | `brightnessctl` work (needs restart)
sudo usermod -aG video $USER

# Set up Basic AUR Package Helper
git clone https://bitbucket.org/natemaia/baph.git || { echo "Failed cloning baph: $?"; }
cd baph || { echo "Couldn't setup baph, terminating..."; exit 1; }
sudo make install

# Install apps
echo "You're about to install the rest of components required for the key bindings to work."
echo "None of them is a shell dependency, and you're free to change them later."

PS3="Select file manager: "
select fm in thunar caja dolphin nautilus nemo pcmanfm;
do
    break
    read
done

PS3="Select text editor: "
select editor in mousepad atom emacs gedit geany kate vim;
do
    break
    read
done

PS3="Select web browser: "
select browser in chromium brave-bin google-chrome-stable epiphany falkon firefox konqueror midori opera qutebrowser seamonkey surf vivaldi-stable;
do
    break
    read
done

baph -inN $fm $editor $browser

# Install shell
baph -inN nwg-shell

# Run installer (w/o confirmations)
nwg-shell-installer -w
