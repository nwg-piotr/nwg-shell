#!/usr/bin/bash

if [ "$(id -u)" == 0 ] ; then
   echo "Please don't run this script as root"
   exit 1
fi

# Don't continue script if any error occurs.
set -e

function yes_or_no {
	local yn
    while true; do
        read -r -p "$* [y/n]: " yn
        case $yn in
            [Yy]*) choice="Y" ; return 0 ;;
            [Nn]*) choice="n" ; return 0 ;;
        esac
    done
}
echo "Enabling nwg-shell Copr"
sudo dnf copr enable -y tofik/nwg-shell

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
select editor in mousepad emacs gedit geany kate vim;
do
    break
done
echo

PS3="Select web browser: "
select browser in chromium epiphany falkon firefox konqueror midori qutebrowser seamonkey surf;
do
    break
done
echo

echo "Installing selection: $fm $editor $browser"
sudo dnf install -y $fm $editor $browser

echo "Installing nwg-shell"
sudo dnf install -y nwg-shell

echo "Starting from v0.5.0, nwg-shell supports Hyprland Wayland compositor."

echo
yes_or_no "Install Hyprland?"

if [ "$choice" == "Y" ] ; then
   echo "Installing Hyprland"
   dnf install -y hyprland wlr-randr
   echo Installing initial configuration
   nwg-shell-installer -w -hypr
else
   echo Installing initial configuration
   nwg-shell-installer -w
fi

xdg-user-dirs-update
