# Utilities and scripts

## Screenshots: [swappy](https://github.com/jtheoof/swappy)

- Author: Jeremy Attali
- License: MIT

Swappy is a Wayland native snapshot and editor tool, inspired by Snappy on macOS. We use it to make partial screenshots, but it is worth reading the README to find out about other possible applications.

<a href="https://user-images.githubusercontent.com/20579136/179939327-04b634d6-0583-4fbd-b6ab-c955e015b90d.png">![2022-07-20-104012_screenshot](https://user-images.githubusercontent.com/20579136/179939327-04b634d6-0583-4fbd-b6ab-c955e015b90d.png)</a>

## Button bar: [nwg-bar](https://github.com/nwg-piotr/nwg-bar)

- Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/nwg-bar/graphs/contributors)
- License: MIT

The nwg-bar command creates a button bar on the basis of a JSON template placed in the `~/.config/nwg-bar` folder. By default the command displays a horizontal bar in the center of the screen. Nwg-shell uses the bar to display the exit menu, but you may find other uses for it, too.

<a href="https://user-images.githubusercontent.com/20579136/179866515-fe89e50b-cc5f-4878-aeab-387535bc1d94.png">![2022-07-20-014527_screenshot](https://user-images.githubusercontent.com/20579136/179866515-fe89e50b-cc5f-4878-aeab-387535bc1d94.png)</a>

## Icon picker: [nwg-icon-picker](https://github.com/nwg-piotr/nwg-icon-picker)

- Author: Piotr Miller
- License: MIT

Nwg-icon-picker is a tool to search GTK icons by name. Utilized by nwg-panel settings, may also be used system-wide.

![2022-07-20-101601_screenshot](https://user-images.githubusercontent.com/20579136/179932862-c59ac8dd-0ad7-4123-a2e0-e1f7e8121497.png)

## Workflow: [autotiling](https://github.com/nwg-piotr/autotiling)

- Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/autotiling/graphs/contributors)
- License: GPL v3
- Original idea: [Ole Martin Handeland](https://github.com/olemartinorg/i3-alternating-layout)

Sway is a great window manager, but changing layouts manually can be tiring for some users (including me). This script uses the i3ipc-python library to automagically switch the layout splith/splitv, depending on the currently focused window dimensions.

Since v0.2.5 nwg-shell does not use the `autotiling` package, but its own `nwg-autotiling` script, that's better adjusted to use here.

![2022-07-20-033338_screenshot](https://user-images.githubusercontent.com/20579136/179877238-ac4baa65-bc9b-4ad9-8f4f-33d7e22a1c4b.png)

**Important note: turning autotiling on will spoil some default sway behaviour:**

- moving windows with key bindings/swaymsg commands will need you to change the window focus first; dragging windows with Alt+mouse pointer should work well, however;
- stacking and tabbed layouts will behave oddly. If you're attached to them, turn autotiling off, or set the `Depth limit`. Both layouts will work normally back again below the depth limit.
- Split width/hight settings allow to achive uneven 1st window split. You may use them e.g. on vertical outputs, or, together with `depth limit = 2`, to achive the windows behaviour similar to Master/stack DWL layout (`depth_limit = 2`, `splith_width = 0.9`). Both settings are experimental, and may cause some not yet known and unexpected behaviour. Use at you own risk, or set to 1.0 to turn them off.

## System info: [gopsuinfo](https://github.com/nwg-piotr/gopsuinfo)

- Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/gopsuinfo/graphs/contributors)
- License: BSD 2-Clause

This CLI command, based on the [gopsutil](https://github.com/shirou/gopsutil) Go module, produces text output to display system usage info in nwg-panel executors.

![gopsuinfo](https://user-images.githubusercontent.com/20579136/179935626-867cf00c-97b4-4e46-b558-8dbb4ddc4e93.png)
