# nwg-shell project

**The nwg-shell project aims to create a consistent, GTK3-based user interface for the [sway](https://github.com/swaywm/sway) Wayland Compositor. In order to give the user the greatest possible choice, some interface elements provide several alternative solutions. Just installed shell contains a bunch of presets, which can then be freely modified.**

![nwg-shell-header.png](https://raw.githubusercontent.com/nwg-piotr/nwg-shell-resources/master/images/nwg-shell/nwg-shell-header_new2.png)

The project is intended for users of all skill levels. Beginners will find four ready-made and immediately working desktop styles to choose from. Advanced users will get a set of tools to build their own GTK-based user interface. 

> We discourage from editing .dotfiles manually. There's a GUI for that. The configuration files are in json format, which does not forgive mistakes.

The user interface mostly consists of dedicated software, but also uses a couple of great third party products, that perfectly complement our vision. Many thanks to their authors for favorable attitude towards feature requests.

The default (preinstalled) terminal emulator is [foot](https://codeberg.org/dnkl/foot) by Daniel Eklöf. This does not mean that we consider other terminals worse, but that we had to choose one. The remaining elements of the desktop environment, such as the text editor, file manager, web browser, and so on, are left to the user's choice. The author's subjective recommendation might be mousepad, Thunar, and Chromium / Chrome, but it doesn't really make much difference.

On the backend side there's a lot of third party Free Open Source Software. We will try to list all the applications and libraries in Credits.

If you want to share an idea, find a solution to a problem or discuss the project in general, please join [**Discussion**](https://github.com/nwg-piotr/nwg-shell/discussions).

# TOC

- What's inside
    - [Panel: nwg-panel](nwg-panel)
    - [Launcher: nwg-drawer](nwg-drawer)
    - [Dock: nwg-dock](nwg-dock)
    - [Alternative launcher: nwg-menu](nwg-menu)
    - [Notification center: swaync](swaync)
    - [Screen locker: gtklock](gtklock)
    - [Wallpaper management: Azote](azote)
    - [Look and feel: nwg-look](nwg-look)
    - [Display management: nwg-displays](nwg-displays)
    - [Shell settings: nwg-shell-config](nwg-shell-config)
    - [Utilities and scripts](utilities-and-scripts)
- [Where to get](https://nwg-piotr.github.io/nwg-shell/#where-to-get)
- [Recent updates](updates)
- [Credits](https://nwg-piotr.github.io/nwg-shell/#credits)

# Where to get

The default way is to set up nwg-shell on a fresh Arch Linux install, done with the `archinstall` script. A step-by-step guide you'll find in [Wiki](https://github.com/nwg-piotr/nwg-shell/wiki). 

<a href="https://user-images.githubusercontent.com/20579136/182253244-5ebeabfa-853c-4192-b883-686c2d00f20b.png"><img src="https://user-images.githubusercontent.com/20579136/182253244-5ebeabfa-853c-4192-b883-686c2d00f20b.png" width=480></a>

This should work on various Arch derivatives, but expect unexpected. ;) Some packages may be out of date, some other may be missing, and you'll need to install them manually.

<a href="https://user-images.githubusercontent.com/20579136/185012961-2ddbab2a-d9d0-4d58-85e3-9a928effdb46.png"><img src="https://user-images.githubusercontent.com/20579136/185012961-2ddbab2a-d9d0-4d58-85e3-9a928effdb46.png" width=480></a>

<a href="https://user-images.githubusercontent.com/20579136/180582953-6a4bada0-2c27-4139-b60b-78f7c972d6bb.jpeg"><img src="https://user-images.githubusercontent.com/20579136/180582953-6a4bada0-2c27-4139-b60b-78f7c972d6bb.jpeg" width=480></a>

<a href="https://user-images.githubusercontent.com/20579136/185021801-180ad161-89ce-4c72-ae5e-3dce87d8409d.png"><img src="https://user-images.githubusercontent.com/20579136/185021801-180ad161-89ce-4c72-ae5e-3dce87d8409d.png" width=480></a>

<a href="https://user-images.githubusercontent.com/20579136/186039701-e367b2f0-ab9a-4530-b23c-d640e3c6c6a0.png"><img src="https://user-images.githubusercontent.com/20579136/186039701-e367b2f0-ab9a-4530-b23c-d640e3c6c6a0.png" width=480></a>

<a href="https://user-images.githubusercontent.com/20579136/180624922-e4486392-5c91-4896-bb4a-cdf60e6442a0.png"><img src="https://user-images.githubusercontent.com/20579136/180624922-e4486392-5c91-4896-bb4a-cdf60e6442a0.png" width=480></a>

Currently, there is no out-of-the-box installer for other Linux distributions. You may try and install all the components manually.

# Credits

This collection of software depends on numerous third-party programs and libraries, that have not been mentioned above:

- [wlsunset](https://sr.ht/~kennylevinsen/wlsunset) by Kenny Levinsen
- [gtk-layer-shell](https://github.com/wmww/gtk-layer-shell) by Dennis Blommesteijn & William Wold
- [gotk3](https://github.com/gotk3/gotk3) by Conformal Systems LLC
- [gotk3-layershell](https://github.com/dlasky/gotk3-layershell) by [@dlasky](https://github.com/dlasky/gotk3-layershell/commits?author=dlasky) (Dan, thanks again!)
- [go-sway](https://github.com/joshuarubin/go-sway) by Joshua Rubin
- [go-singleinstance](github.com/allan-simon/go-singleinstance) by 2015 Allan Simon
- [python-i3ipc](https://github.com/altdesktop/i3ipc-python) by Tony Crisci
- [python-psutil](https://github.com/giampaolo/psutil) by Jay Loden, Dave Daeschler & Giampaolo Rodola
- [python-geopy](https://github.com/geopy/geopy) by Kostya Esmukov
- [python-dasbus](https://github.com/rhinstaller/dasbus) by Red Hat Installer Engineering Team
- [python-netifaces](https://github.com/stephica/netifaces) by Alastair Houghton
- [python-requests](https://github.com/psf/requests) by Python Software Foundation
- [brightnessctl](https://github.com/Hummer12007/brightnessctl) by Mykyta Holuakha
- [ddcutil](https://github.com/rockowitz/ddcutil) by Sanford Rockowitz
- [playerctl](https://github.com/altdesktop/playerctl) by Tony Crisci
- [wlr-randr]() by Simon Ser
- [PulseAudio](https://www.freedesktop.org/wiki/Software/PulseAudio), [bluez-utils](http://www.bluez.org), and probably more, which we forgot to mention here. Please forgive us, if so.
 
 [GTK](https://gitlab.gnome.org/GNOME/gtk) and related libraries are a free and open-source cross-platform widget toolkit for creating graphical user interfaces, developed by The GNOME Project.
 
 [sway](https://github.com/swaywm/sway) is an i3-compatible Wayland compositor Copyright (c) 2016-2017 Drew DeVault.
 
<div style="padding: 10px 0px"></div>

<img src="https://github.com/nwg-piotr/nwg-shell-resources/raw/master/resources/logo.svg" width="32" align="left" style="vertical-align: inline; padding: 0px 10px 0px 0px">The author of the [project logo](https://github.com/nwg-piotr/nwg-shell-resources/blob/master/resources/logo.svg) is [edskeye](https://github.com/edskeye).

The artwork used on this site is licensed under the terms of the [Creative Commons Zero v1.0 Universal license](https://github.com/nwg-piotr/nwg-shell-wallpapers/blob/main/LICENSE), and has been contributed by:

- [@badkarma](https://forum.archlabslinux.com/u/badkarma/summary) on the ArchLabs Linux forum
- [SGS](https://github.com/sgse)
- [nwg-piotr](https://github.com/nwg-piotr)

# This project is supported by

<a href="https://jb.gg/OpenSourceSupport"><img width="300" src="https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.png" alt="JetBrains Logo (Main) logo."></a>

Copyright © 2000-2022 JetBrains s.r.o. JetBrains and the JetBrains logo are registered trademarks of JetBrains s.r.o.
