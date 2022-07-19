# nwg-shell project

The nwg-shell project aims to create a consistent GTK3-based user interface for the [sway](https://github.com/swaywm/sway) Wayland Compositor. In order to give the user the greatest possible choice, some interface elements provide several alternative solutions. Freshly installed shell contains a bunch of presets, which can then be freely modified.

![nwg-shell-header.png](https://raw.githubusercontent.com/nwg-piotr/nwg-shell-resources/master/images/nwg-shell/nwg-shell-header_new2.png)

The user interface mostly consists of dedicated software, but also uses a couple of great third party products ([swaync](https://github.com/ErikReider/SwayNotificationCenter), [gtklock](https://github.com/jovanlanik/gtklock)), that perfectly complement our vision. Many thanks to their authors for favorable attitude towards feature requests.

The default (preinstalled) terminal is [foot](https://codeberg.org/dnkl/foot). This does not mean that we consider other terminals worse, but that we had to choose one. The remaining elements of the desktop environment, such as the text editor, file manager or web browser, and so on, are left to the user's choice. The author's subjective recommendation might be mousepad, Thunar, and Chromium / Chrome, but it doesn't really make much difference.

On the backend side there's a lot of third party Free Open Source Software. We will try to list them all in Credits.

## Panel: [nwg-panel](https://github.com/nwg-piotr/nwg-panel)

Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/nwg-panel/graphs/contributors)

License: MIT

The panel is the central point of the project. At the moment it contains 12 modules: Clock, Controls, CustomButton, Executor, MenuStart, OpenWeather, Playerctl, Scratchpad, SwayNC (integrates Eric Reider's [SwayNotificationCenter](https://github.com/ErikReider/SwayNotificationCenter)), SwayTaskbar, SwayWorkspaces and Tray. The Executor module supports tint2-like executors, that allow to display user-defined content. The MenuStart module adds support for the nwg-menu launcher.

![2022-07-19-101927_screenshot](https://user-images.githubusercontent.com/20579136/179712622-52ef164a-6dc6-4893-be16-98bac92fd150.png)


The Controls drop-down window provides brightness and volume controls and switching audio outputs. It also includes user-definable menu items.

## Application launcher: [nwg-drawer](https://github.com/nwg-piotr/nwg-drawer)

Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/nwg-drawer/graphs/contributors)

License: MIT

The `nwg-drawer` command displays the application grid. The search entry allows to look for installed applications, and for files in XDG user directories. The grid view may also be filtered by categories. You may pin applications by right-clicking them. Pinned items will appear above the grid. Right-click a pinned item to unpin it.

![2022-07-19-113502_screenshot](https://user-images.githubusercontent.com/20579136/179719429-e21bb41b-acdf-4d3e-a095-5d9acad8ef21.png)

## Dock: [nwg-dock](https://github.com/nwg-piotr/nwg-dock)

The author's personal choice is to see the running tasks in the nwg-panel's SwayTaskbar. If you prefer to use a dock, however, this may be the choice for you. Nwg-dock features pinned buttons, task buttons, workspace switcher and the launcher button. The latter by default starts nwg-drawer.

![2022-07-19-122405_screenshot](https://user-images.githubusercontent.com/20579136/179729044-6e15cb8a-9bca-45a4-ad48-d0271782dce0.png)

