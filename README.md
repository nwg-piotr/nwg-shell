# nwg-shell

[![Packaging status](https://repology.org/badge/vertical-allrepos/nwg-shell.svg)](https://repology.org/project/nwg-shell/versions)

This project is an attempt to create a GTK-based shell for [sway](https://github.com/swaywm/sway) Wayland compositor. It's aimed at those, who do not believe
that the rationale of the modern computer is to use less than 200 MiB RAM and 0.5% CPU. Those who don't want to stare solely at the terminal's black window.
The programs included in the project are to give you the freedom of choice what your desktop looks like.

![nwg-shell-header.png](https://raw.githubusercontent.com/nwg-piotr/nwg-shell-resources/master/images/nwg-shell/nwg-shell-header_new2.png)

The installer provided in this repository pulls all the necessary dependencies, and preconfigures 4 desktop
styles for you to choose from. Each of them you can modify freely from the nwg-shell-config GUI. Or you may choose 
the 'Custom' preset to experiment with.

## Installation

### The hard way (v0.2 available)

[How to set up nwg-shell on minimal Arch Linux install in several simple steps](https://github.com/nwg-piotr/nwg-shell/wiki) - Wiki

### The easy way (v0.2 not yet available)

Install [ArchLabs Linux](https://archlabslinux.com) with preconfigured sway session.

## Components, as for now:

### [nwg-panel](https://github.com/nwg-piotr/nwg-panel) (Python)

[![Packaging status](https://repology.org/badge/vertical-allrepos/nwg-panel.svg)](https://repology.org/project/nwg-panel/versions)

The panel is the central point of the project. At the moment it contains 11 modules: Clock, Controls, CustomButton, 
Executor, MenuStart, Playerctl, Scratchpad, SwayNC (integrates Eric Reider's 
[SwayNotificationCenter](https://github.com/ErikReider/SwayNotificationCenter)), SwayTaskbar SwayWorkspaces and Tray. 
The Executor module supports tint2-like executors, that allow to add user-defined features. The MenuStart module adds 
support for the nwg-menu plugin (see below).

![nwg-panel.png](https://raw.githubusercontent.com/nwg-piotr/nwg-shell-resources/master/images/nwg-shell/nwg-panel1.png)

### [nwg-dock](https://github.com/nwg-piotr/nwg-dock) (Go)

[![Packaging status](https://repology.org/badge/vertical-allrepos/nwg-dock.svg)](https://repology.org/project/nwg-dock/versions)

Fully configurable dock written in Go. It features pinned buttons, task buttons, workspace switcher and launcher button. The latter by default starts
nwg-drawer.

![nwg-dock.png](https://raw.githubusercontent.com/nwg-piotr/nwg-shell-resources/master/images/nwg-shell/nwg-dock1.png)

### [nwg-menu](https://github.com/nwg-piotr/nwg-menu) (Go)

[![Packaging status](https://repology.org/badge/vertical-allrepos/nwg-menu.svg)](https://repology.org/project/nwg-menu/versions)

The MenuStart plugin to nwg-panel, written in Go. It displays the system menu with simplified [freedesktop main categories](https://specifications.freedesktop.org/menu-spec/latest/apa.html). It also provides the search entry,
to look for installed application on the basis of .desktop files, and for files in XDG user directories.

You may pin-up applications above the categories list. In the bottom-right corner of the window you'll also see a set of buttons: lock screen, logout,
restart and shutdown.

![nwg-menu.png](https://raw.githubusercontent.com/nwg-piotr/nwg-shell-resources/master/images/nwg-shell/nwg-menu.png)

### [nwg-drawer](https://github.com/nwg-piotr/nwg-drawer) (Go)

[![Packaging status](https://repology.org/badge/vertical-allrepos/nwg-drawer.svg)](https://repology.org/project/nwg-drawer/versions)

A golang replacement to the `nwggrid` command (a part of nwg-launchers). The `nwg-drawer` command displays the application grid. The search entry allows to look
for installed applications, and for files in XDG user directories. The grid view may also be filtered by categories. You may pin applications by right-clicking
them. Pinned items will appear above the grid. Right-click a pinned item to unpin it.

![nwg-drawer.png](https://raw.githubusercontent.com/nwg-piotr/nwg-shell-resources/master/images/nwg-shell/nwg-drawer.png)

### [nwg-bar](https://github.com/nwg-piotr/nwg-bar) (Go)

[![Packaging status](https://repology.org/badge/vertical-allrepos/nwg-bar.svg)](https://repology.org/project/nwg-bar/versions)

nwg-bar is a golang replacement to the `nwgbar` command (a part of [nwg-launchers](https://github.com/nwg-piotr/nwg-launchers)), with some improvements. 
Aimed at sway, works with wlroots-based compositors only. The `nwg-bar` command creates a button bar on the basis of a JSON template placed in the 
`~/.config/nwg-bar` folder. By default the command displays a horizontal bar in the center of the screen. Use command line arguments to change the placement.

![nwg-bar.png](https://raw.githubusercontent.com/nwg-piotr/nwg-shell-resources/master/images/nwg-shell/nwg-bar.png)

### [Azote](https://github.com/nwg-piotr/azote) (Python)

[![Packaging status](https://repology.org/badge/vertical-allrepos/azote.svg)](https://repology.org/project/azote/versions)

Azote is a picture browser and background setter, as the frontend to the swaybg (sway/Wayland) and feh (X windows) commands. The user interface is being
developed with multi-headed setups in mind. Azote also includes several colour management tools.

![azote.png](https://raw.githubusercontent.com/nwg-piotr/nwg-shell-resources/master/images/nwg-shell/azote.png)

### [nwg-displays](https://github.com/nwg-piotr/nwg-displays) (Python)

[![Packaging status](https://repology.org/badge/vertical-allrepos/nwg-displays.svg)](https://repology.org/project/nwg-displays/versions)

Output management utility inspired by wdisplays and wlay. The program provides an intuitive GUI to manage multiple 
displays, apply settings, save outputs configuration and workspace -> output assignments to text files, which you
then include in the sway config file.

![nwg-displays](https://raw.githubusercontent.com/nwg-piotr/nwg-shell-resources/master/images/nwg-displays/nwg-displays.png)

### [nwg-look](https://github.com/nwg-piotr/nwg-look) (Go)

[![Packaging status](https://repology.org/badge/vertical-allrepos/nwg-look.svg)](https://repology.org/project/nwg-look/versions)

Nwg-look is a GTK3 settings editor, designed to work properly in wlroots-based Wayland environment.
The look and feel is strongly influenced by [LXAppearance](https://wiki.lxde.org/en/LXAppearance),
but nwg-look is intended to free the user from a few inconveniences:

- It works natively on Wayland. You no longer need Xwayland, nor strange env variables for it to run.
- It applies gsettings directly, with no need to use
[workarounds](https://github.com/swaywm/sway/wiki/GTK-3-settings-on-Wayland). You don't need to set
 gsettings in the sway config file. You don't need the `import-gsettings` script any longer.

![nwg-look](https://raw.githubusercontent.com/nwg-piotr/nwg-shell-resources/master/images/nwg-look/nwg-look.png)

### [nwg-wrapper](https://github.com/nwg-piotr/nwg-wrapper) (Python)

[![Packaging status](https://repology.org/badge/vertical-allrepos/nwg-wrapper.svg)](https://repology.org/project/nwg-wrapper/versions)

This program is a GTK3-based wrapper to display a script output, or a text file content on the desktop in sway or 
other wlroots-based compositors. It uses the [gtk-layer-shell](https://github.com/wmww/gtk-layer-shell) library
to place the window on the bottom layer. As well the script output, at the text file may be formatted with 
[Pango Markup](https://developer.gnome.org/pygtk/stable/pango-markup-language.html). The window appearance is defined
with css styling.

![nwg-wrapper.png](https://raw.githubusercontent.com/nwg-piotr/nwg-shell-resources/master/images/nwg-shell/nwg-wrapper.png)

### [gopsuinfo](https://github.com/nwg-piotr/gopsuinfo) (Go)

[![Packaging status](https://repology.org/badge/vertical-allrepos/gopsuinfo.svg)](https://repology.org/project/gopsuinfo/versions)

This command, based on the [gopsutil](https://github.com/shirou/gopsutil) Go module, produces text output to display system usage info in nwg-panel executors.

### [autotiling](https://github.com/nwg-piotr/autotiling) (Python)

[![Packaging status](https://repology.org/badge/vertical-allrepos/autotiling.svg)](https://repology.org/project/autotiling/versions)

This script uses the [i3ipc-python library](https://github.com/altdesktop/i3ipc-python) to switch the layout splith/splitv depending on the currently focused
window dimensions. It works on both sway and i3 window managers. You may love it or hate it, but it's my must have.

![nwg-shell-config.png](https://raw.githubusercontent.com/nwg-piotr/nwg-shell-resources/master/images/nwg-shell/autotiling.png)

## [nwg-shell-config](https://github.com/nwg-piotr/nwg-shell-config)

As you see, the nwg-shell project is a DIY kit with elements to chose from. However, together with the 
[ArchLabs Linux](https://archlabslinux.com) team, we decided to develop a GUI to configure all the components in one 
place. To give users more complete control over the system, we also integrated several third-party programs. 
This required some interference with the basic sway config, using included files, that are modified on the fly from the 
GUI level.

![nwg-shell-config.png](https://raw.githubusercontent.com/nwg-piotr/nwg-shell-resources/master/images/nwg-shell/nwg-shell-config-02.png)

## Support for other WMs

This project is primarily aimed at sway. Some parts may work on other wlroots-based compositors. Some may even work on X11, but it's not the primary objective. Feel free to submit addons / improvements, but keep in mind that all the stuff **must** work on sway, and **may or may not** work elsewhere.

### Pull requests adding support for non-sway stuff 

are welcome.

### Feature requests like "add <place_your_wm_here> support"

go to `/dev/null`.

## Contributions

If you like the idea of the GTK shell for sway, feel free to submit your improvements, new modules, plugins or standalone programs. Preferred languages are python and Go.

**Important: before you open a PR containing major changes to already existing programs, please (PLEASE!) open an issue to discuss what you're going to do.**

### Feedback

Bug reports and ideas are more than welcome. Please remember, however, that at this stage, most part of the shell is being developed by a single hobbyist, who uses
Arch Linux (BTW). Some issues specific to other environment, e.g. Debian, FreeBSD, are out of my range and need some Community commitment.

## Resources

The project logo has been created by [edskeye](https://github.com/edskeye). You'll find the basic svg file in the
[resources](https://github.com/nwg-piotr/nwg-shell-resources/tree/master/resources) repository.

<div align="center"><img src="https://raw.githubusercontent.com/nwg-piotr/nwg-shell-resources/master/images/nwg-shell/logo.png"/></div>

Images used on this page come from:

- https://wallhaven.cc/w/6kxmj6
- https://wallhaven.cc/w/o39669
- https://pixabay.com/illustrations/home-mountains-fantasy-floating-5889366
- https://pixabay.com/vectors/mobile-devices-website-mockup-web-2017978

## Credits

This collection of software relies on some great third-party programs and libraries:

- [wlsunset](https://sr.ht/~kennylevinsen/wlsunset) by Kenny Levinsen
- [SwayNotificationCenter](https://github.com/ErikReider/SwayNotificationCenter) by Eric Reider
- [swappy](https://github.com/jtheoof/swappy) Copyright (c) 2020 Jeremy Attali
- [gtk-layer-shell](https://github.com/wmww/gtk-layer-shell) Copyright (c) 2014 Dennis Blommesteijn, Copyright (c) 2020 William Wold
- [gotk3](https://github.com/gotk3/gotk3) Copyright (c) 2013-2014 Conformal Systems LLC,
Copyright (c) 2015-2018 gotk3 contributors
- [gotk3-layershell](https://github.com/dlasky/gotk3-layershell) by [@dlasky](https://github.com/dlasky/gotk3-layershell/commits?author=dlasky) - many thanks for writing this software, and for patience with my requests!
- [go-sway](https://github.com/joshuarubin/go-sway) Copyright (c) 2019 Joshua Rubin
- [go-singleinstance](github.com/allan-simon/go-singleinstance) Copyright (c) 2015 Allan Simon
- [python-i3ipc](https://github.com/altdesktop/i3ipc-python) Copyright (c) 2015, Tony Crisci
- [python-psutil](https://github.com/giampaolo/psutil) Copyright (c) 2009, Jay Loden, Dave Daeschler, Giampaolo Rodola
- [python-geopy](https://github.com/geopy/geopy) by Kostya Esmukov
- [brightnessctl](https://github.com/Hummer12007/brightnessctl) Copyright (c) 2016 Mykyta Holuakha
- [playerctl](https://github.com/altdesktop/playerctl) by Tony Crisci
- [PulseAudio](https://www.freedesktop.org/wiki/Software/PulseAudio), 
[bluez-utils](http://www.bluez.org), [python-netifaces](https://archlinux.org/packages/community/x86_64/python-netifaces),
 and probably more, which I forgot to mention here. Please forgive me, if so.

[sway](https://github.com/swaywm/sway) is an i3-compatible Wayland compositor Copyright (c) 2016-2017 Drew DeVault
