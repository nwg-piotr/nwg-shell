# nwg-shell project

**The nwg-shell project aims to create a consistent GTK3-based user interface for the [sway](https://github.com/swaywm/sway) Wayland Compositor. In order to give the user the greatest possible choice, some interface elements provide several alternative solutions. Just installed shell contains a bunch of presets, which can then be freely modified.**

![nwg-shell-header.png](https://raw.githubusercontent.com/nwg-piotr/nwg-shell-resources/master/images/nwg-shell/nwg-shell-header_new2.png)

The user interface mostly consists of dedicated software, but also uses a couple of great third party products ([swaync](https://github.com/ErikReider/SwayNotificationCenter), [gtklock](https://github.com/jovanlanik/gtklock)), that perfectly complement our vision. Many thanks to their authors for favorable attitude towards feature requests.

The default (preinstalled) terminal is [foot](https://codeberg.org/dnkl/foot). This does not mean that we consider other terminals worse, but that we had to choose one. The remaining elements of the desktop environment, such as the text editor, file manager or web browser, and so on, are left to the user's choice. The author's subjective recommendation might be mousepad, Thunar, and Chromium / Chrome, but it doesn't really make much difference.

On the backend side there's a lot of third party Free Open Source Software. We will try to list them all in Credits.

# What's inside

## Panel: [nwg-panel](https://github.com/nwg-piotr/nwg-panel)

- Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/nwg-panel/graphs/contributors)
- License: MIT

The panel is the central point of the project. At the moment it contains 13 modules: BrightnessSlider, Clock, Controls, CustomButton, Executor, MenuStart, OpenWeather, Playerctl, Scratchpad, SwayNC (integrates Eric Reider's [SwayNotificationCenter](https://github.com/ErikReider/SwayNotificationCenter)), SwayTaskbar, SwayWorkspaces and Tray. The Executor module supports tint2-like executors, that allow to display user-defined content. The MenuStart module adds support for the nwg-menu launcher.

<a href="https://user-images.githubusercontent.com/20579136/179712622-52ef164a-6dc6-4893-be16-98bac92fd150.png">![2022-07-19-101927_screenshot](https://user-images.githubusercontent.com/20579136/179712622-52ef164a-6dc6-4893-be16-98bac92fd150.png)</a>

The Controls drop-down window provides brightness & volume controls, and audio output switcher. It also includes user-customizable menu items.

![image](https://user-images.githubusercontent.com/20579136/179860809-34dd4449-1cee-46c0-bd70-2f970aacc46d.png)

## Application launcher: [nwg-drawer](https://github.com/nwg-piotr/nwg-drawer)

- Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/nwg-drawer/graphs/contributors)
- License: MIT

The `nwg-drawer` command displays the application grid. The search entry allows to look for installed applications, and for files in XDG user directories. The grid view may also be filtered by categories. You may pin applications by right-clicking them. Pinned items will appear above the grid. Right-click a pinned item to unpin it.

<a href="https://user-images.githubusercontent.com/20579136/179719429-e21bb41b-acdf-4d3e-a095-5d9acad8ef21.png">![2022-07-19-113502_screenshot](https://user-images.githubusercontent.com/20579136/179719429-e21bb41b-acdf-4d3e-a095-5d9acad8ef21.png)</a>

## Dock: [nwg-dock](https://github.com/nwg-piotr/nwg-dock)

- Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/nwg-dock/graphs/contributors)
- License: MIT

The author's personal preference is to see the running tasks in the nwg-panel's SwayTaskbar. If you prefer to use a dock, however, this may be the choice for you. Nwg-dock features pinned buttons, task buttons, workspace switcher and the launcher button. The latter by default starts nwg-drawer. The dock may be placed on the bottom, top or left side.

<a href="https://user-images.githubusercontent.com/20579136/179729044-6e15cb8a-9bca-45a4-ad48-d0271782dce0.png">![2022-07-19-122405_screenshot](https://user-images.githubusercontent.com/20579136/179729044-6e15cb8a-9bca-45a4-ad48-d0271782dce0.png)</a>

## Alternative launcher: [nwg-menu](https://github.com/nwg-piotr/nwg-menu)

- Author: Piotr Miller
- License: MIT

If you've recently parted ways with Windows, you may miss the menu button. This program, which is also an nwg-panel plugin, will help you acclimatize. It displays the system menu with simplified [freedesktop main categories](https://specifications.freedesktop.org/menu-spec/latest/apa.html). It also provides the search entry, to look for installed application on the basis of .desktop files, and for files in XDG user directories. You may pin-up applications above the categories list. In the bottom-right corner of the window you'll also see a set of buttons: lock screen, logout, restart and shutdown.

Due to limited interest, the development of this launcher may be discontinued in the future. Enjoy while you can. ;)

<a href="https://user-images.githubusercontent.com/20579136/179743263-a314bf97-00b0-4720-b0ed-8bdb4844e6bd.png">![2022-07-19-134851_screenshot](https://user-images.githubusercontent.com/20579136/179743263-a314bf97-00b0-4720-b0ed-8bdb4844e6bd.png)</a>

## Notification center: [swaync](https://github.com/ErikReider/SwayNotificationCenter)

- Author: Erik Reider
- License: GPL v3

This program provides the notification daemon and a GTK-based user interface for managing notifications. Nwg-shell integrates swaync, adding a panel notification icon and configuration options in own config utility.

<a href="https://user-images.githubusercontent.com/20579136/179748788-1929c74e-64f8-4280-80d1-45f02972f1ef.png">![2022-07-19-141124_screenshot](https://user-images.githubusercontent.com/20579136/179748788-1929c74e-64f8-4280-80d1-45f02972f1ef.png)</a>

## Screen locker: [gtklock](https://github.com/jovanlanik/gtklock)

- Author: Jovan Lanik
- License: GPL v3

The shell uses gtklock as the default locker in the Idle & Lock screen settings. We add a random image background (local or from unsplash.com), and (optionally) a media player control window over the lock screen.

<a href="https://user-images.githubusercontent.com/20579136/179752612-f245bc38-d113-4f82-8d42-556ac5438a70.png">![2022-07-19-143850_screenshot](https://user-images.githubusercontent.com/20579136/179752612-f245bc38-d113-4f82-8d42-556ac5438a70.png)</a>

Alternatively, as a locker you can use the well-known [swaylock](https://github.com/swaywm/swaylock) by Drew DeVault.

## Wallpaper management: [Azote](https://github.com/nwg-piotr/azote)

- Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/azote/graphs/contributors)
- License: GPL v3

Azote is an image viewer with options useful when using them as wallpapers: clipping, mirroring, splitting between several displays. For setting the background, the program uses Drew DeVault's [swaybg](https://github.com/swaywm/swaybg) (sway/Wayland) and Tom Gilbert's & Daniel Frieselfeh's [feh](https://feh.finalrewind.org) (X windows) commands. The user interface is being developed with multi-headed setups in mind. Azote also includes several colour management tools, as e.g. color picker or palettes creation on the basis of an image.

<a href="https://user-images.githubusercontent.com/20579136/179864696-11c5c93d-f86b-487d-a508-edb885157506.png">![2022-07-20-012458_screenshot](https://user-images.githubusercontent.com/20579136/179864696-11c5c93d-f86b-487d-a508-edb885157506.png)</a>


## Look and feel: [nwg-look](https://github.com/nwg-piotr/nwg-look)

- Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/nwg-look)
- License: MIT

Nwg-look is a GTK3 settings editor, designed to work properly in wlroots-based Wayland environment. The look and feel is strongly influenced by [LXAppearance](https://wiki.lxde.org/en/LXAppearance), but nwg-look frees the user from a few inconveniences, by applying setting directly. It provides changing gtk themes, icon themes, cursors, and also tuning some other GTK settings.

![2022-07-19-172154_screenshot](https://user-images.githubusercontent.com/20579136/179790068-856f2e7f-1d87-4212-9341-e1ca55586bc9.png)

## Display management: [nwg-displays](https://github.com/nwg-piotr/nwg-displays)

- Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/nwg-displays/graphs/contributors)
- License: MIT

This program provides an intuitive GUI to manage multiple displays, and save outputs configuration and workspace to output assignments.

![2022-07-20-011519_screenshot](https://user-images.githubusercontent.com/20579136/179864328-2dd5aa8b-dac9-4eaf-893c-cb85215a212c.png)

## Shell settings: [nwg-shell-config](https://github.com/nwg-piotr/nwg-shell-config)

- Author: Piotr Miller & [Contributors](https://github.com/nwg-piotr/nwg-shell-config/graphs/contributors)
- License: MIT

You may use the nwg-shell components as a DIY kit with pieces to choose from. This program is a GUI to configure all the components in one place, together with the most essential third-party applications. This involves significant interference with the basic sway config, using included files, that are modified on the fly from the GUI level. Even though you no longer need to edit "dotfiles" manually, you can still do it if you want. Not recommended for beginners.

![2022-07-20-020818_screenshot](https://user-images.githubusercontent.com/20579136/179869662-ed91b9a7-1490-4e06-9693-9dab1db29e54.png)

## Utilities and scripts

### Button bar: nwg-bar

- Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/nwg-bar/graphs/contributors)
- License: MIT

The nwg-bar command creates a button bar on the basis of a JSON template placed in the `~/.config/nwg-bar` folder. By default the command displays a horizontal bar in the center of the screen. Nwg-shell uses the bar to display the exit menu, but you may find other uses for it, too.

<a href="https://user-images.githubusercontent.com/20579136/179866515-fe89e50b-cc5f-4878-aeab-387535bc1d94.png">![2022-07-20-014527_screenshot](https://user-images.githubusercontent.com/20579136/179866515-fe89e50b-cc5f-4878-aeab-387535bc1d94.png)</a>

### Desktop widgets: [nwg-wrapper](https://github.com/nwg-piotr/nwg-wrapper)

- Authors: Piotr Miller & [Contributors](https://github.com/nwg-piotr/nwg-wrapper/graphs/contributors)
- License: MIT

On tiling window managers, putting widgets on the desktop is basically pointless, as they remain invisible 99% of the time. There happen exceptions, however. Nwg-wrapper alows to display a script output, or a Pango-formatted text file content, and we use it to create the keyboard shortcuts help for beginners.

<a href="https://user-images.githubusercontent.com/20579136/179868205-26c579e2-c113-4e03-85c5-2220cbd81c5d.png">![2022-07-20-015655_screenshot](https://user-images.githubusercontent.com/20579136/179868205-26c579e2-c113-4e03-85c5-2220cbd81c5d.png)</a>

# Project supported by

<a href="https://jb.gg/OpenSourceSupport"><img width="300" src="https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.png" alt="JetBrains Logo (Main) logo."></a>

Copyright © 2000-2022 JetBrains s.r.o. JetBrains and the JetBrains logo are registered trademarks of JetBrains s.r.o.
