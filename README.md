# nwg-shell

This project is an attempt to create a GTK-based shell for [sway](https://github.com/swaywm/sway) Wayland compositor. It's aimed at those who do not believe 
that the point of a modern computer is that it should use less than 200 MiB RAM and 0.5% CPU. Those who don't want to stare solely at the terminal's black window.
The programs included in the project are to give you the freedom of choice what your desktop looks like.

![3.png](https://scrot.cloud/images/2021/05/09/3.png)

*This project is primarily aimed at sway. Some parts may work on other wlroots-based compositors. Some may even work on X11, but it's not the primary objective.
Feel free to submit addons / improvements, but keep in mind that all the stuff **must** work on sway, and **may or may not** work elsewhere.*

*Probably "nwg-shell" is not the best possible name. It's subject to change as soon as someone comes up with a better idea.*

## Components, as for now:

### [nwg-panel](https://github.com/nwg-piotr/nwg-panel)

A GTK3-based panel is the central point of the project. For now it contains 8 modules and 1 external plugin. It also supports tin2-like executors, that allow
to add user-defined features easily.

### [nwg-launchers](https://github.com/nwg-piotr/nwg-launchers)

A set of GTK-based launchers: application grid, button bar and dmenu. I initially wrote them in python, but it turned out to be too slow. I developed them from
scratch in C++, as my first, and probably the last C++ code. Thanks to Contributors, led by [@Siborgium](https://github.com/Siborgium), the code looks pretty well
now, but I understand hardly anything. I'm not going to live long enough to learn C++, so I'll code the grid and dmenu from scratch in golang sooner or later.

### [nwg-dock](https://github.com/nwg-piotr/nwg-dock)

Fully configurable dock written in Go. It features pinned buttons, task buttons, the workspace switcher and the launcher button. The latter by default starts 
nwggrid (application grid) from nwg-launchers.

### [nwg-menu](https://github.com/nwg-piotr/nwg-menu)

It's the MenuStart plugin to nwg-panel written in Go. It's also capable of working standalone.

### [Azote](https://github.com/nwg-piotr/azote)

Azote is a GTK+3-based picture browser and background setter, as the frontend to the swaybg (sway/Wayland) and feh (X windows) commands. The user interface is being developed with multi-headed setups in mind. Azote also includes several colour management tools.

### [gopsuinfo](https://github.com/nwg-piotr/gopsuinfo)

A [gopsutil](https://github.com/shirou/gopsutil)-based command to display system usage info as text in panels like Waybar or icon/text in tint2 and nwg-panel executors.

### [autotiling](https://github.com/nwg-piotr/autotiling)

This script uses the [i3ipc-python library](https://github.com/altdesktop/i3ipc-python) to switch the layout splith/splitv depending on the currently focused
window dimensions. It works on both sway and i3 window managers. You may love it or hate it, but it's my must have.
