# nwg-shell

This project is an attempt to create a GTK-based shell for [sway](https://github.com/swaywm/sway) Wayland compositor. It's aimed at those, who do not believe
that the rationale of the modern computer is to use less than 200 MiB RAM and 0.5% CPU. Those who don't want to stare solely at the terminal's black window.
The programs included in the project are to give you the freedom of choice what your desktop looks like.

![3.png](https://scrot.cloud/images/2021/05/09/3.png)

*This project is primarily aimed at sway. Some parts may work on other wlroots-based compositors. Some may even work on X11, but it's not the primary objective.
Feel free to submit addons / improvements, but keep in mind that all the stuff **must** work on sway, and **may or may not** work elsewhere.*

## Components, as for now:

### [nwg-panel](https://github.com/nwg-piotr/nwg-panel) (Python)

The panel is the central point of the project. At the moment it contains 9 modules: Clock, Controls, CustomButton, Executor, MenuStart, Playerctl,
Scratchpad, SwayTaskbar and SwayWorkspaces. The Executor module supports tint2-like executors, that allow to add user-defined features.
The MenuStart module adds support for the nwg-menu plugin (see below).

### [nwg-dock](https://github.com/nwg-piotr/nwg-dock) (Go)

Fully configurable dock written in Go. It features pinned buttons, task buttons, the workspace switcher and the launcher button. The latter by default starts
nwggrid (application grid) from nwg-launchers.

<div align="center"><img src="https://scrot.cloud/images/2021/05/10/dock.png" width="400"/></div>

### [nwg-menu](https://github.com/nwg-piotr/nwg-menu) (Go)

It's the MenuStart plugin to nwg-panel, written in Go. It displays the system menu with simplified [freedesktop main categories](https://specifications.freedesktop.org/menu-spec/latest/apa.html). It also provides the search entry,
to look for installed application on the basis of .desktop files, and for files in XDG user directories.

You may pin-up applications above the categories list. In the bottom-right corner of the window you'll also see a set of buttons: lock screen, logout,
restart and shutdown.

<div align="center"><img src="https://scrot.cloud/images/2021/05/10/menu.png" width="400"/></div>

### [nwg-drawer](https://github.com/nwg-piotr/nwg-drawer) (Go)

A golang replacement to the `nwggrid` command (a part of nwg-launchers). The `nwg-drawer` command displays the application grid. The search entry allows to look
for installed applications, and for files in XDG user directories. The grid view may also be filtered by categories. You may pin applications by right-clicking
them. Pinned items will appear above the grid. Right-click a pinned item to unpin it.

<div align="center"><img src="https://scrot.cloud/images/2021/05/30/screenshot-01.png" width="400"/></div>

### [nwg-bar](https://github.com/nwg-piotr/nwg-bar) (Go, beta)

nwg-bar is a golang replacement to the `nwgbar` command (a part of [nwg-launchers](https://github.com/nwg-piotr/nwg-launchers)), with some improvements. 
Aimed at sway, works with wlroots-based compositors only. The `nwg-bar` command creates a button bar on the basis of a JSON template placed in the 
`~/.config/nwg-bar` folder. By default the command displays a horizontal bar in the center of the screen. Use command line arguments to change the placement.

<div align="center"><img src="https://scrot.cloud/images/2021/07/01/screenshot.png" width="400"/></div>

### [Azote](https://github.com/nwg-piotr/azote) (Python)

Azote is a picture browser and background setter, as the frontend to the swaybg (sway/Wayland) and feh (X windows) commands. The user interface is being
developed with multi-headed setups in mind. Azote also includes several colour management tools.

<div align="center"><img src="https://scrot.cloud/images/2021/03/13/azote-1.9.0.png" width="400"/></div>

### [gopsuinfo](https://github.com/nwg-piotr/gopsuinfo) (Go)

This command, based on the [gopsutil](https://github.com/shirou/gopsutil) Go module, produces text output to display system usage info in nwg-panel executors.

### [autotiling](https://github.com/nwg-piotr/autotiling) (Python)

This script uses the [i3ipc-python library](https://github.com/altdesktop/i3ipc-python) to switch the layout splith/splitv depending on the currently focused
window dimensions. It works on both sway and i3 window managers. You may love it or hate it, but it's my must have.

## Contributions

If you like the idea of the GTK shell for sway, feel free to submit your improvements, new modules, plugins or standalone programs. Preferred languages are python and Go.

**Important: before you open a PR containing major changes to already existing programs, please (PLEASE!) open an issue to discuss what you're going to do.**

### Feedback

Bug reports and ideas are more than welcome. Please remember, however, that at this stage, most part of the shell is being developed by a single hobbyist, who uses
Arch Linux (BTW). Some issues specific to other environment, e.g. Debian, FreeBSD, are out of my range and need some Community commitment.

### [Project tracker](https://github.com/users/nwg-piotr/projects/2)

## Resources

The initial version of the shell logo was created by [SGSE](https://github.com/sgse), and it looked well. Having
received some users' feedback, I decided to use another one, due to unwanted religious associations. The current
version has been created by [edskeye](https://github.com/edskeye). You'll find the basic svg file in the
[resources](https://github.com/nwg-piotr/nwg-shell/tree/main/resources) folder.

<div align="center"><img src="https://scrot.cloud/images/2021/05/30/shell-logo-basic-render5b2cd1cc090aab3a.png"/></div>

Images used on this page come from:

- https://wallhaven.cc/w/6kxmj6
- https://wallhaven.cc/w/o39669
- https://pixabay.com/illustrations/home-mountains-fantasy-floating-5889366
- https://pixabay.com/vectors/mobile-devices-website-mockup-web-2017978
