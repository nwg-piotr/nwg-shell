#!/usr/bin/bash

# This script should go to /usr/bin, or somewhere else on #PATH

if [ "$(id -u)" == 0 ] ; then
   echo "Please don't run this script as root"
   exit 1
fi

# Don't continue script if any error occurs.
set -e

function yes_or_no {
    while true; do
        read -r -p "$* [y/n]: " yn
        case $yn in
            [Yy]*) choice="Y" ; return 0 ;;
            [Nn]*) choice="n" ; return 0 ;;
        esac
    done
}

# This is not really necessary, may be removed if case you insist
sudo pacman -S --noconfirm xdg-user-dirs
echo Initializing XDG user directories
xdg-user-dirs-update

# Needed for brightnessctl to work
echo "Adding $USER to video group"
sudo usermod -aG video $USER

# nwg-shell needs a file manager, a text editor and a web browser preinstalled
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
select browser in chromium brave-bin google-chrome epiphany falkon firefox konqueror microsoft-edge-stable-bin midori opera qutebrowser seamonkey surf vivaldi;
do
    break
done
echo

echo "Installing selection: $fm $editor $browser"
sudo pacman -S --noconfirm $fm $editor $browser

# We need at least sway, but it's optional in the nwg-shell package
echo Installing sway
sudo pacman -S --noconfirm sway

echo Installing nwg-shell
sudo pacman -S --noconfirm nwg-shell

# Hyprland installation is up to the users taste
echo "Starting from v0.5.0, nwg-shell supports Hyprland Wayland compositor."
echo
yes_or_no "Install Hyprland?"

if [ "$choice" == "Y" ] ; then
   echo "Installing Hyprland"
   sudo pacman -S --noconfirm hyprland wlr-randr
   echo Installing initial configuration
   # Install configs for sway and Hyprland
   nwg-shell-installer -w -hypr
else
   echo Installing initial configuration
   # Install configs for just sway
   nwg-shell-installer -w
fi
