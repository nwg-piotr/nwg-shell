# nwg-shell project

**The nwg-shell project aims to create a consistent, GTK3-based user interface for the [sway](https://github.com/swaywm/sway) Wayland Compositor. In order to give the user the greatest possible choice, some interface elements provide several alternative solutions. Just installed shell contains a bunch of presets, which can then be freely modified.**

![nwg-shell-header.png](https://raw.githubusercontent.com/nwg-piotr/nwg-shell-resources/master/images/nwg-shell/nwg-shell-header_new2.png)

<div align="center"><a href="https://github.com/nwg-piotr/nwg-shell-resources/blob/master/resources/logo.svg"><img src="https://github.com/nwg-piotr/nwg-shell-resources/raw/master/resources/logo.svg" width="64"></a></div>

The user interface mostly consists of dedicated software, but also uses a couple of great third party products, that perfectly complement our vision. Many thanks to their authors for favorable attitude towards feature requests.

The default (preinstalled) terminal emulator is [foot](https://codeberg.org/dnkl/foot) by Daniel Eklöf. This does not mean that we consider other terminals worse, but that we had to choose one. The remaining elements of the desktop environment, such as the text editor, file manager, web browser, and so on, are left to the user's choice. The author's subjective recommendation might be mousepad, Thunar, and Chromium / Chrome, but it doesn't really make much difference.

On the backend side there's a lot of third party Free Open Source Software. We will try to list all the applications and libraries in Credits.

# TOC

- [What's inside](https://nwg-piotr.github.io/nwg-shell/#whats-inside)
    - [Panel: nwg-panel](https://nwg-piotr.github.io/nwg-shell#panel-nwg-panel)
    - [Launcher: nwg-drawer](https://nwg-piotr.github.io/nwg-shell#launcher-nwg-drawer)
    - [Dock: nwg-dock](https://nwg-piotr.github.io/nwg-shell/#dock-nwg-dock)
    - [Alternative launcher: nwg-menu](https://nwg-piotr.github.io/nwg-shell#alternative-launcher-nwg-menu)
    - [Notification center: swaync](https://nwg-piotr.github.io/nwg-shell/#notification-center-swaync)
    - [Screen locker: gtklock](https://nwg-piotr.github.io/nwg-shell/#screen-locker-gtklock)
    - [Wallpaper management: Azote](https://nwg-piotr.github.io/nwg-shell/#wallpaper-management-azote)
    - [Look and feel: nwg-look](https://nwg-piotr.github.io/nwg-shell/#look-and-feel-nwg-look)
    - [Display management: nwg-displays](https://nwg-piotr.github.io/nwg-shell/#display-management-nwg-displays)
    - [Shell settings: nwg-shell-config](https://nwg-piotr.github.io/nwg-shell/#shell-settings-nwg-shell-config)
    - [Utilities and scripts](https://nwg-piotr.github.io/nwg-shell/#utilities-and-scripts)
- [Where to get](https://nwg-piotr.github.io/nwg-shell/#where-to-get)
- [Credits](https://nwg-piotr.github.io/nwg-shell/#credits)

# What's inside

## Panel: [nwg-panel](https://github.com/nwg-piotr/nwg-panel)

- Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/nwg-panel/graphs/contributors)
- License: MIT

The panel is the central point of the project. At the moment it contains 13 modules: BrightnessSlider, Clock, Controls, CustomButton, Executor, MenuStart, OpenWeather, Playerctl, Scratchpad, SwayNC (integrates Eric Reider's [SwayNotificationCenter](https://github.com/ErikReider/SwayNotificationCenter)), SwayTaskbar, SwayWorkspaces and Tray. The Executor module supports tint2-like executors, that allow to display user-defined content. The MenuStart module adds support for the nwg-menu launcher.

<a href="https://user-images.githubusercontent.com/20579136/179712622-52ef164a-6dc6-4893-be16-98bac92fd150.png">![2022-07-19-101927_screenshot](https://user-images.githubusercontent.com/20579136/179712622-52ef164a-6dc6-4893-be16-98bac92fd150.png)</a>

The Controls drop-down window provides brightness & volume controls, and audio output switcher. It also includes user-customizable menu items.

![image](https://user-images.githubusercontent.com/20579136/179860809-34dd4449-1cee-46c0-bd70-2f970aacc46d.png)

## Launcher: [nwg-drawer](https://github.com/nwg-piotr/nwg-drawer)

- Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/nwg-drawer/graphs/contributors)
- License: MIT

Nwg-drawer is the primary launcher, and displays the application grid. The search entry allows to look for installed applications, and for files in XDG user directories. The grid view may also be filtered by categories. You may pin applications by right-clicking them. They will appear above the grid. Right-click an item to unpin it.

<a href="https://user-images.githubusercontent.com/20579136/179719429-e21bb41b-acdf-4d3e-a095-5d9acad8ef21.png">![2022-07-19-113502_screenshot](https://user-images.githubusercontent.com/20579136/179719429-e21bb41b-acdf-4d3e-a095-5d9acad8ef21.png)</a>

## Dock: [nwg-dock](https://github.com/nwg-piotr/nwg-dock)

- Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/nwg-dock/graphs/contributors)
- License: MIT

The author's personal preference is to see the running tasks in the nwg-panel's SwayTaskbar. If you prefer to use a dock, however, this may be the choice for you. Nwg-dock features pinned buttons, task buttons, workspace switcher and the launcher button. The latter by default starts nwg-drawer. The dock may be placed on the bottom, top or left side.

<a href="https://user-images.githubusercontent.com/20579136/179729044-6e15cb8a-9bca-45a4-ad48-d0271782dce0.png">![2022-07-19-122405_screenshot](https://user-images.githubusercontent.com/20579136/179729044-6e15cb8a-9bca-45a4-ad48-d0271782dce0.png)</a>

## Alternative launcher: [nwg-menu](https://github.com/nwg-piotr/nwg-menu)

- Author: Piotr Miller
- License: MIT

If you've recently parted ways with Windows, you may miss the menu button. This launcher will help you acclimatize. It displays the system menu with simplified [freedesktop main categories](https://specifications.freedesktop.org/menu-spec/latest/apa.html). It also provides the search entry, to look for installed application on the basis of .desktop files, and for files in XDG user directories. You may pin-up applications above the categories list. In the bottom-right corner of the window you'll also see a set of buttons: lock screen, logout, restart and shutdown.

Due to limited interest, the development of this launcher may be discontinued in the future. Enjoy while you can. ;)

<a href="https://user-images.githubusercontent.com/20579136/179743263-a314bf97-00b0-4720-b0ed-8bdb4844e6bd.png">![2022-07-19-134851_screenshot](https://user-images.githubusercontent.com/20579136/179743263-a314bf97-00b0-4720-b0ed-8bdb4844e6bd.png)</a>

## Notification center: [swaync](https://github.com/ErikReider/SwayNotificationCenter)

- Author: Erik Reider
- License: GPL v3

This program provides the notification daemon and a GTK-based user interface for managing notifications. Nwg-shell integrates swaync, by adding a panel notification icon and configuration options in own config utility.

<a href="https://user-images.githubusercontent.com/20579136/179748788-1929c74e-64f8-4280-80d1-45f02972f1ef.png">![2022-07-19-141124_screenshot](https://user-images.githubusercontent.com/20579136/179748788-1929c74e-64f8-4280-80d1-45f02972f1ef.png)</a>

## Screen locker: [gtklock](https://github.com/jovanlanik/gtklock)

- Author: Jovan Lanik
- License: GPL v3

The shell uses gtklock as the default locker in the 'Idle & Lock screen' settings. We add a random image background (local or from unsplash.com), and (optionally) a media player control window over the lock screen.

<a href="https://user-images.githubusercontent.com/20579136/179752612-f245bc38-d113-4f82-8d42-556ac5438a70.png">![2022-07-19-143850_screenshot](https://user-images.githubusercontent.com/20579136/179752612-f245bc38-d113-4f82-8d42-556ac5438a70.png)</a>

Alternatively, as a locker you can use the well-known [swaylock](https://github.com/swaywm/swaylock) by Drew DeVault.

## Wallpaper management: [Azote](https://github.com/nwg-piotr/azote)

- Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/azote/graphs/contributors)
- License: GPL v3

Azote is an image browser with options useful when using them as wallpapers: clipping, mirroring, splitting between displays. For setting the background, the program uses Drew DeVault's [swaybg](https://github.com/swaywm/swaybg) (sway/Wayland) and Tom Gilbert's & Daniel Frieselfeh's [feh](https://feh.finalrewind.org) (X windows) commands. The user interface is being developed with multi-headed setups in mind. Azote also includes several colour management tools, as e.g. color picker or palettes creation on the basis of an image.

<a href="https://user-images.githubusercontent.com/20579136/179864696-11c5c93d-f86b-487d-a508-edb885157506.png">![2022-07-20-012458_screenshot](https://user-images.githubusercontent.com/20579136/179864696-11c5c93d-f86b-487d-a508-edb885157506.png)</a>


## Look and feel: [nwg-look](https://github.com/nwg-piotr/nwg-look)

- Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/nwg-look)
- License: MIT

Nwg-look is a GTK3 settings editor, designed to work properly in wlroots-based Wayland environment. The look and feel is strongly influenced by [LXAppearance](https://wiki.lxde.org/en/LXAppearance), but nwg-look frees the user from a few inconveniences, by applying setting directly. It provides changing gtk themes, icon themes, cursors, and also tuning some other GTK settings.

![2022-07-19-172154_screenshot](https://user-images.githubusercontent.com/20579136/179790068-856f2e7f-1d87-4212-9341-e1ca55586bc9.png)

## Display management: [nwg-displays](https://github.com/nwg-piotr/nwg-displays)

- Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/nwg-displays/graphs/contributors)
- License: MIT

This program provides an intuitive GUI to manage multiple displays, save outputs configuration and workspace-to-output assignments.

![2022-07-20-011519_screenshot](https://user-images.githubusercontent.com/20579136/179864328-2dd5aa8b-dac9-4eaf-893c-cb85215a212c.png)

## Shell settings: [nwg-shell-config](https://github.com/nwg-piotr/nwg-shell-config)

- Author: Piotr Miller & [Contributors](https://github.com/nwg-piotr/nwg-shell-config/graphs/contributors)
- License: MIT

This program is a GUI to configure all the components in one place, together with the most essential third-party applications. This involves significant interference with the basic sway config, using included files, that are modified on the fly from the GUI level. Even though you no longer need to edit "dotfiles" manually, you can still do it if you need to (not recommended for beginners).

Nwg-shell-config allows to set the common sway preferences (screen, input devices, idle and lock screen configuration, main applications key bindings), as well as switch between predefined desktop styles. Each of the above may be adjusted to user's taste, that includes placement of the application drawer, dock, exit menu, and notification center.

![2022-07-20-020818_screenshot](https://user-images.githubusercontent.com/20579136/179869662-ed91b9a7-1490-4e06-9693-9dab1db29e54.png)

## Utilities and scripts

### Screenshots: [swappy](https://github.com/jtheoof/swappy)

- Author: Jeremy Attali
- License: MIT

Swappy is a Wayland native snapshot and editor tool, inspired by Snappy on macOS. We use it to make partial screenshots, but it is worth reading the README to find out about other possible applications.

<a href="https://user-images.githubusercontent.com/20579136/179939327-04b634d6-0583-4fbd-b6ab-c955e015b90d.png">![2022-07-20-104012_screenshot](https://user-images.githubusercontent.com/20579136/179939327-04b634d6-0583-4fbd-b6ab-c955e015b90d.png)</a>

### Button bar: [nwg-bar](https://github.com/nwg-piotr/nwg-bar)

- Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/nwg-bar/graphs/contributors)
- License: MIT

The nwg-bar command creates a button bar on the basis of a JSON template placed in the `~/.config/nwg-bar` folder. By default the command displays a horizontal bar in the center of the screen. Nwg-shell uses the bar to display the exit menu, but you may find other uses for it, too.

<a href="https://user-images.githubusercontent.com/20579136/179866515-fe89e50b-cc5f-4878-aeab-387535bc1d94.png">![2022-07-20-014527_screenshot](https://user-images.githubusercontent.com/20579136/179866515-fe89e50b-cc5f-4878-aeab-387535bc1d94.png)</a>

### Desktop widgets: [nwg-wrapper](https://github.com/nwg-piotr/nwg-wrapper)

- Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/nwg-wrapper/graphs/contributors)
- License: MIT

On tiling window managers, putting widgets on the desktop is basically pointless, as they remain invisible 99% of the time. There happen exceptions, however. Nwg-wrapper alows to display a script output, or a Pango-formatted text file content, and we use it to create the keyboard shortcuts help for beginners.

<a href="https://user-images.githubusercontent.com/20579136/179868205-26c579e2-c113-4e03-85c5-2220cbd81c5d.png">![2022-07-20-015655_screenshot](https://user-images.githubusercontent.com/20579136/179868205-26c579e2-c113-4e03-85c5-2220cbd81c5d.png)</a>

### Icon picker: [nwg-icon-picker](https://github.com/nwg-piotr/nwg-icon-picker)

- Author: Piotr Miller
- License: MIT

Nwg-icon-picker is a tool to search GTK icons by name. Utilized by nwg-panel settings, may also be used system-wide.

![2022-07-20-101601_screenshot](https://user-images.githubusercontent.com/20579136/179932862-c59ac8dd-0ad7-4123-a2e0-e1f7e8121497.png)

### Workflow: [autotiling](https://github.com/nwg-piotr/autotiling)

- Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/autotiling/graphs/contributors)
- License: GPL v3
- Original idea: [Ole Martin Handeland](https://github.com/olemartinorg/i3-alternating-layout)

Sway is a great window manager, but changing layouts manually can be tiring for some users (including me). This script uses the i3ipc-python library to automagically switch the layout splith/splitv, depending on the currently focused window dimensions.

![2022-07-20-033338_screenshot](https://user-images.githubusercontent.com/20579136/179877238-ac4baa65-bc9b-4ad9-8f4f-33d7e22a1c4b.png)

### System info: [gopsuinfo](https://github.com/nwg-piotr/gopsuinfo)

- Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/gopsuinfo/graphs/contributors)
- License: BSD 2-Clause

This CLI command, based on the [gopsutil](https://github.com/shirou/gopsutil) Go module, produces text output to display system usage info in nwg-panel executors.

![gopsuinfo](https://user-images.githubusercontent.com/20579136/179935626-867cf00c-97b4-4e46-b558-8dbb4ddc4e93.png)

# Where to get

The easiest and fastest way is to install [ArchLabs Linux](https://archlabslinux.com), whose sway session is nothing but a full nwg-shell implementation. 

A slightly more complicated way is to set up nwg-shell on a fresh Arch Linux install, done with the `archinstall` script. A step-by-step guide you'll find in [Wiki](https://github.com/nwg-piotr/nwg-shell/wiki). This should probably work on Arch derivatives other than ArchLabs, but we have never tried. ;)

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
 
The artwork used on this site is licensed under the terms of the [Creative Commons Zero v1.0 Universal license](https://github.com/nwg-piotr/nwg-shell-wallpapers/blob/main/LICENSE), and has been contributed by:

- [@badkarma](https://forum.archlabslinux.com/u/badkarma/summary) on the ArchLabs Linux forum
- [SGS](https://github.com/sgse)
- [nwg-piotr](https://github.com/nwg-piotr)

<img src="https://github.com/nwg-piotr/nwg-shell-resources/raw/master/resources/logo.svg" width="32" align="left" style="vertical-align: text-bottom; padding: 0px 10px 10px 0px">The author of the [project logo](https://github.com/nwg-piotr/nwg-shell-resources/blob/master/resources/logo.svg) is [edskeye](https://github.com/edskeye).

# This project is supported by

<a href="https://jb.gg/OpenSourceSupport"><img width="300" src="https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.png" alt="JetBrains Logo (Main) logo."></a>

Copyright © 2000-2022 JetBrains s.r.o. JetBrains and the JetBrains logo are registered trademarks of JetBrains s.r.o.
