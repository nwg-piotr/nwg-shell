# nwg-shell project

The nwg-shell project aims to create a consistent GTK3-based user interface for the [sway](https://github.com/swaywm/sway) Wayland Compositor. In order to give the user the greatest possible choice, some interface elements provide several alternative solutions. Freshly installed shell contains a bunch of presets, which can then be freely modified.

![nwg-shell-header.png](https://raw.githubusercontent.com/nwg-piotr/nwg-shell-resources/master/images/nwg-shell/nwg-shell-header_new2.png)

The user interface mostly consists of its own dedicated software, but also uses a couple of great third party products ([swaync](https://github.com/ErikReider/SwayNotificationCenter), [gtklock](https://github.com/jovanlanik/gtklock)), that perfectly complement our vision. Many thanks to their authors for favorable attitude towards feature requests.

The default (preinstalled) terminal is [foot](https://codeberg.org/dnkl/foot). This does not mean that we consider other terminals designed to work in the Wayland environment worse, but that we had to choose one. The remaining elements of the desktop environment, such as the text editor, file manager or web browser, and so on, are left to the user's choice. The author's subjective recommendation might be mousepad, Thunar, and Chromium / Chrome, but it doesn't really make much difference.

On the backend side there's a lot of Free Open Source Software. We will try to list them all in Credits.

## Panel: [nwg-panel](https://github.com/nwg-piotr/nwg-panel)

Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/nwg-panel/graphs/contributors)

License: MIT

The panel is the central point of the project. At the moment it contains 12 modules: Clock, Controls, CustomButton, Executor, MenuStart, OpenWeather, Playerctl, Scratchpad, SwayNC (integrates Eric Reider's [SwayNotificationCenter](https://github.com/ErikReider/SwayNotificationCenter)), SwayTaskbar, SwayWorkspaces and Tray. The Executor module supports tint2-like executors, that allow to display user-defined content. The MenuStart module adds support for the nwg-menu launcher.

![image](https://user-images.githubusercontent.com/20579136/179702698-bd2dc505-07a4-4c70-88b5-fe681248bc88.png)

<div align="center"><a href="<img src="https://raw.githubusercontent.com/nwg-piotr/nwg-shell-resources/master/images/nwg-shell-config/preset-0.png" width="640"/>"><img src="https://raw.githubusercontent.com/nwg-piotr/nwg-shell-resources/master/images/nwg-shell-config/preset-0.png" width="640"/></a></div>

The Controls drop-down window provides brightness and volume controls and switching audio outputs. It also includes user-definable menu items.

