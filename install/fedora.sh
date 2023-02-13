#!/usr/bin/bash

if [ "$(id -u)" == 0 ] ; then
   echo "Please don't run this script as root"
   exit 1
fi

# Don't continue script if any error occurs.
set -e

echo "Enabling nwg-shell Copr"
sudo dnf copr enable -y tofik/nwg-shell

echo "Enabling pamixer Copr"
sudo dnf copr enable -y notahat/pamixer

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
sudo dnf install -y nwg-shell pamixer

echo "Installing initial configuration"
# Version in fedora does not support -w flag, so, implemented workaround
echo y | nwg-shell-installer -a

xdg-user-dirs-update
