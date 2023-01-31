#!/usr/bin/bash

# Download me, make executable, run & remove:
# wget https://raw.github.com/nwg-piotr/nwg-shell/gui/install/test.sh -O test.sh && chmod u+x test.sh && ./test.sh && rm arch.sh

echo "You're about to install the rest of components required for the key bindings to work."
echo "None of them is a shell dependency, and you're free to change them later."

PS3="Select file manager: "
select fm in thunar caja dolphin nautilus nemo pcmanfm;
do
    break
done

PS3="Select text editor: "
select editor in mousepad atom emacs gedit geany kate vim;
do
    break
done

PS3="Select web browser: "
select browser in chromium brave-bin google-chrome-stable epiphany falkon firefox konqueror midori opera qutebrowser seamonkey surf vivaldi-stable;
do
    break
done

echo "baph -inN $fm $editor $browser"
