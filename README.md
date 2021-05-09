# nwg-shell

This project is an attempt to create a GTK-based shell for [sway](https://github.com/swaywm/sway) Wayland compositor. It's aimed at those, who do not believe 
that the point of a modern computer is to use less than 200 MiB RAM and 0.5% CPU. Those who don't want to stare solely at the terminal's black window.
The programs included in the project are to give you the freedom of choice what your desktop looks like.

![3.png](https://scrot.cloud/images/2021/05/09/3.png)

*This project is primarily aimed at sway. Some parts may work on other wlroots-based compositors. Some may even work on X11, but it's not the primary objective.
Feel free to submit addons / improvements, but keep in mind that all the stuff **must** work on sway, and **may or may not** work elsewhere.*

*Probably "nwg-shell" is not the best possible name. It's subject to change as soon as someone comes up with a better idea.*

## Components, as for now:

### [nwg-panel](https://github.com/nwg-piotr/nwg-panel)

The panel is the central point of the project. At the moment it contains 9 modules: Clock, Controls, CustomButton, Executor, MenuStart, Playerctl,
Scratchpad, SwayTaskbar and SwayWorkspaces. The Executor module supports tint2-like executors, that allow to add user-defined features. 
The MenuStart module adds support for the nwg-menu plugin.

### [nwg-launchers](https://github.com/nwg-piotr/nwg-launchers)

This is a set of launchers: application grid, button bar and dmenu. Initially written in python, turned out to be too slow. I developed them from
scratch in C++, as my first, and probably the last C++ code. Thanks to Contributors, led by [@Siborgium](https://github.com/Siborgium), the code looks pretty well
now, but it's difficult to me to maintain. I'm not going to live long enough to learn C++ at last, so I think I'll code the grid and dmenu from scratch in golang 
sooner or later.

### [nwg-dock](https://github.com/nwg-piotr/nwg-dock)

Fully configurable dock written in Go. It features pinned buttons, task buttons, the workspace switcher and the launcher button. The latter by default starts 
nwggrid (application grid) from nwg-launchers.


<div align="center"><img src="https://scrot.cloud/images/2021/05/10/dock.png" width="400"/></div>

### [nwg-menu](https://github.com/nwg-piotr/nwg-menu)

It's the MenuStart plugin to nwg-panel, written in Go. It displays the system menu with simplified [freedesktop main categories](https://specifications.freedesktop.org/menu-spec/latest/apa.html). It also provides the search entry,
to look for installed application on the basis of .desktop files, and for files in XDG user directories.

You may pin-up applications above the categories list. In the bottom-right corner of the window you'll also see a set of buttons: logout, lock screen, 
restart and shutdown.

<div align="center"><img src="https://scrot.cloud/images/2021/05/10/menu.png" width="400"/></div>

### [Azote](https://github.com/nwg-piotr/azote)

Azote is a picture browser and background setter, as the frontend to the swaybg (sway/Wayland) and feh (X windows) commands. The user interface is being 
developed with multi-headed setups in mind. Azote also includes several colour management tools.

<div align="center"><img src="https://scrot.cloud/images/2021/03/13/azote-1.9.0.png" width="300"/></div>

### [gopsuinfo](https://github.com/nwg-piotr/gopsuinfo)

This command, based on the [gopsutil](https://github.com/shirou/gopsutil) Go module, produces text output to display system usage info in nwg-panel executors.

### [autotiling](https://github.com/nwg-piotr/autotiling)

This script uses the [i3ipc-python library](https://github.com/altdesktop/i3ipc-python) to switch the layout splith/splitv depending on the currently focused
window dimensions. It works on both sway and i3 window managers. You may love it or hate it, but it's my must have.

## Resources

The shell logo has been created by [SGSE](https://github.com/sgse) and released under the terms of the Creative Commons license 
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.en). Available as .svg in the resources folder.

<div align="center"><img src="https://scrot.cloud/images/2021/05/10/nwg-shell-logo-cyan.png"/></div>

Images used on this page come from:

- https://wallhaven.cc/w/6kxmj6
- https://wallhaven.cc/w/o39669
- https://pixabay.com/illustrations/home-mountains-fantasy-floating-5889366
- https://pixabay.com/vectors/mobile-devices-website-mockup-web-2017978
