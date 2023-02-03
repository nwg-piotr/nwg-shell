#!/usr/bin/bash

if [ "$(id -u)" == 0 ] ; then
   echo "Please don't run this script as root"
   exit 1
fi

# Don't continue script if any error occurs.
set -e

# wget https://raw.github.com/nwg-piotr/nwg-shell/main/install/arch-dev.sh && chmod u+x arch-dev.sh && ./arch-dev.sh && rm ./arch-dev.sh
sudo pacman -S --noconfirm git man-db vi xdg-user-dirs

echo Initializing XDG user directories
xdg-user-dirs-update

echo "Adding $USER to video group"
sudo usermod -aG video $USER

echo "Installing Basic AUR Package Helper"
git clone https://bitbucket.org/natemaia/baph.git || { echo "Failed cloning baph: $?"; }
cd baph || { echo "Couldn't setup baph, terminating..."; exit 1; }
sudo make install

echo
echo "You're about to select components, that need to be preinstalled for the key bindings to work."
echo "None of above is a shell dependency, and you're free to change them any time later."
echo

PS3="Select file manager: "
select fm in thunar caja dolphin nautilus nemo pcmanfm;
do
    break
done
echo

PS3="Select text editor: "
select editor in mousepad atom emacs gedit geany kate vim;
do
    break
done
echo

PS3="Select web browser: "
select browser in chromium brave-bin google-chrome epiphany falkon firefox konqueror midori opera qutebrowser seamonkey surf vivaldi;
do
    break
done
echo

echo "Installing selection: $fm $editor $browser"
baph -inN $fm $editor $browser

echo Installing nwg-shell
baph -inN nwg-shell-git

echo Installing initial configuration
nwg-shell-installer -w
