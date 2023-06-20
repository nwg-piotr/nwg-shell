#!/usr/bin/bash

if [ "$(id -u)" == 0 ] ; then
   echo "Please don't run this script as root"
   exit 1
fi

function yes_or_no {
    while true; do
        read -r -p "$* [y/n]: " yn
        case $yn in
            [Yy]*) choice="Y" ; return 0 ;;
            [Nn]*) choice="n" ; return 1 ;;
        esac
    done
}

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
select browser in chromium brave-bin google-chrome epiphany falkon firefox konqueror microsoft-edge-stable-bin midori opera qutebrowser seamonkey surf vivaldi;
do
    break
done
echo

echo "Installing selection: $fm $editor $browser"
baph -inN $fm $editor $browser

echo Installing Simon Ser GPG key, needed by the wlr-randr AUR package
gpg --recv-key 0FDE7BE0E88F5E48

echo Installing nwg-shell
baph -inN nwg-shell

echo "Starting from v0.5.0, nwg-shell supports Hyprland Wayland compositor."

echo
yes_or_no "Install Hyprland?"

if [ "$choice" == "Y" ] ; then
   echo "Installing Hyprland"
   baph -inN hyprland wlr-randr
   echo Installing initial configuration
   nwg-shell-installer -w -hypr
else
   echo Installing initial configuration
   nwg-shell-installer -w
fi
