#!/usr/bin/bash

if [ "$(id -u)" == 0 ] ; then
   echo "Please don't run this script as root"
   exit 1
fi

# Don't continue script if any error occurs.
set -e

# Check fedora version
source /etc/os-release

version=$REDHAT_SUPPORT_PRODUCT_VERSION

echo "Enabling nwg-shell Copr"
sudo curl https://copr.fedorainfracloud.org/coprs/tofik/nwg-shell/repo/fedora-$version/tofik-nwg-shell-fedora-$version.repo -o /etc/yum.repos.d/nwg-shell.repo
sudo curl https://copr.fedorainfracloud.org/coprs/tofik/sway/repo/fedora-${version}/tofik-sway-fedora-${version}.repo -o /etc/yum.repos.d/tofik-sway.repo
sudo curl https://copr.fedorainfracloud.org/coprs/erikreider/SwayNotificationCenter/repo/fedora-${version}/erikreider-SwayNotificationCenter-fedora-${version}.repo -o /etc/yum.repos.d/erikreider-SwayNotificationCenter.repo
sudo curl https://copr.fedorainfracloud.org/coprs/mochaa/gtk-session-lock/repo/fedora-${version}/mochaa-gtk-session-lock-fedora-${version}.repo -o /etc/yum.repos.d/mochaa-gtk-session-lock.repo

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

echo "Installing selection: $fm $editor $browser and nwg-shell"
rpm-ostree install --allow-inactive $fm $editor $browser nwg-shell 

echo "Apply changes live to make nwg-shell-installer available"
sudo rpm-ostree apply-live

echo "Installing initial configuration"
# Version in fedora does not support -w flag, so, implemented workaround
echo y | nwg-shell-installer -a

xdg-user-dirs-update
