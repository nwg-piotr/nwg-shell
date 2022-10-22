# Recent updates

## nwg-shell 0.3.5

- some fixes to presets and css style sheets

### Related

### nwg-shell-config 0.4.3

**Support for gtklock 2.x**

- powerbar module suspend command
- powerbar module userswitch command
- powerbar module logout command

Thanks to @jovanlanik for additions and bug fixes to [gtklock](https://github.com/jovanlanik/gtklock) and [gtklock-playerctl-module](https://github.com/jovanlanik/gtklock-playerctl-module).

**Translations**

Modified keys: 

- `"power-off-tooltip"`
- `"reboot-tooltip"`
- `"under-clock"`

New keys: 

- `"suspend"`
- `"suspend-tooltip"`
- `"logout"`
- `"logout-tooltip"`
- `"switch-user"`
- `"switch-user-tooltip"`

### nwg-panel 0.7.12

- Playerctl module: full (unshortened) label text -> tooltip text;
- Controls module: added optional, semi-transparent background window to click and close the popup, in addition to the previous behaviour;
- some typos fixed by @kianmeng;
- added fallback icon name, same as the `app_id`, when all other icon name detection methods fail.

## nwg-shell-config 0.4.2 (2022.10.16)

- added Brazilian Portuguese `pt_BR` by [rb-andrade](https://github.com/rb-andrade)
- updated Dutch translation `nl_NL` by [Peppe](https://forum.archlabslinux.com/u/Peppe)

## nwg-shell-config 0.4.1 (2022.10.15)

**[Bug in default settings]** The previous version contains a typo in default gtklock time format: the leading apostrophe will prevent gtklock from starting. Please check your settings, and remove it, if exists.

![image](https://user-images.githubusercontent.com/20579136/195958457-7d916ceb-3db6-4b1c-9f10-4cde8c628700.png)

## nwg-dock 0.3.1 (2022.10.14)

- workspaces button fixed for touch screens
- minor code cleanup

## nwg-shell-config 0.4.0 (2022.10.13)

Added support for translations. The `~/.local/share/nwg-shell/data` json file contains the `"interface-locale"` key, that is empty by default. It means: use auto-detected locale. Detection looks like this:

```python
lang = os.getenv("LANG").split(".")[0] if not shell_data["interface-locale"] else shell_data["interface-locale"]
```

which returns e.g. `pl_PL` for the `pl_PL.UTF-8` locale, __if no value found__ in the data file. Otherwise the saved value will be used. You may use the "Interface language" combo to save the value. This is supposed to work shell-wide in the future.

### Localization authors, so far:

- `fr_FR` by **[@giraudan](https://github.com/giraudan)**
- `it_IT` by **[@luftmensch-luftmensh](https://github.com/luftmensch-luftmensch)**
- `nl_NL` by **[@Peppe](https://forum.archlabslinux.com/u/Peppe)**
- `pl_PL` by **[@nwg-piotr](https://github.com/nwg-piotr)**

## nwg-panel 0.7.11 (2022.10.13)

- added check for the max value returned by `brightnessctl` (bug fixed)

## nwg-panel 0.7.10 (2022.10.07)

- Playerctl module: added album cover (since everyone does it).

![image](https://user-images.githubusercontent.com/20579136/194442974-e45208e3-6573-4e96-92a5-3034c0cbe6f9.png)

## nwg-panel 0.7.9 (2022.10.06)

- added (back) check box to disable the panel homogeneity. See #95: if we use Center modules in a panel, the panel's box "columns" need to be homogeneous, if we want the center columns content (e.g. clock) to be centered in the screen. If some columns width exceeds 1/3 of the screen width, it results in cutting off the panel edges. If one really needs 3 columns and wide content, the only solution is to turn the columns' homogeneity off, and give up on centering.
- Playerctl module: added possibility to scroll track metadata longer than the label length limit (instead of shortening).

![image](https://user-images.githubusercontent.com/20579136/194182330-dbd749a4-2ff0-4f47-b7da-5d768f04dc8e.png)

## nwg-shell 0.3.4 (2022.10.04)

- added `nwg-shell-installer --restore` flag, to bring back missing configs, styles & data files;
- added common and per-preset @jovanlanik's gtklock modules settings;
- added gtklock per-preset style sheets;
- added support for the gtklock playerctl module;
- added support for @ErikReider's swaync mpris widget;
- fixed updates check + some other minor fixes.

![2022-10-04-013414_screenshot](https://user-images.githubusercontent.com/20579136/193704413-b7645004-b2e1-40d9-8198-ae03beda4a65.png)

## nwg-drawer 0.3.1 (2022.09.25)

- fixed crash on trimming long names/descriptions;
- added support for `Hidden`, `OnlyShowIn` and `NotShowIn`; 
- fixed path to own data dir;
- minor code improvements.

## nwg-panel 0.7.8 (2022.09.13)

- one more [fix to scaling tray icons](https://github.com/nwg-piotr/nwg-panel/commit/90ad8679546e2e6158f7af306b702b2c2080458f).

## nwg-shell 0.3.0 / 0.3.3 (2022.09.09-10)

This release brings the graphical updater, that replaces the former `nwg-shell-installer -u` CLI command. You'll be notified about shell updates via system notifications with 'Update' and 'Later' actions. If you decide to update later, you may open the shell config utility, and use the 'Updates' button. It will show the number of pending updates, if any. 

_NOTE: I found out that the default background was missing from fresh v0.3.0 installs, and got into trouble while trying to fix it quickly, so we are on v0.3.3 now._

![2022-09-09-032942_screenshot](https://user-images.githubusercontent.com/20579136/189253420-d32bd451-13c9-45ae-a420-a1966d1de154.png)

![2022-09-09-033424_screenshot](https://user-images.githubusercontent.com/20579136/189253801-dc1894c1-5fde-4192-858c-a475cbd0022b.png)

The 0.3.0 version also  simplifies the installation process. You no longer need to edit the `/etc/environment` file, as all the helper scripts are now being installed to `/usr/local/bin` by the nwg-shell package itself. Applying the 0.3.0 update to the existing shell installation will remove no longer necessary scripts from your home directory.

- [nwg-shell 0.3.0 release notes](https://github.com/nwg-piotr/nwg-shell/releases/tag/v0.3.0)
- [nwg-shell-config 0.3.12 release notes](https://github.com/nwg-piotr/nwg-shell-config/releases/tag/v0.3.12)

## nwg-shell 0.2.5 (2022.09.02)

This release replaces the `autotiling` script (package) with the `nwg-autotiling` command (nwg-shell-config entry point). This is to avoid adding the shell-specific stuff to the original script, as it's quite widely used outside the project. All the arguments remain the same. The new script is better tailored to the shell, and should be more stable.

**Related:**

### nwg-panel

- fixed improper Tray icon size on outputs scaled up;
- fixed output dimensions detection on compositors other than sway.

### nwg-displays

- fixed initial resolution for scaled displays (by @nvski);
- config migrated from mistakenly named `~/.config/nwg-outputs` to `~/.config/nwg-displays`.

### gopsuinfo 0.1.2

- added attempt to read k10temp_tctl temperature sensor.

## nwg-shell 0.2.4 (2022.08.29)

Since the ArchLabs 2022.08.21 release, sway, as well as nwg-shell, are no longer included. If you'd like to use them on AL anyway, see [Discussions](https://github.com/nwg-piotr/nwg-shell/discussions/17).

The 0.2.4 release simplifies some key bindings in the main sway config file, and adds 2 buttons to panel presets.  Also some minor bugs in related css files have been fixed. Performing the upgrade will overwrite your sway config file, panel presets, and panel css style sheets will the new defaults. Your current sway config file will be backed up during the upgrade process. Changes you made to panel presets 0-3 will be lost. You may want to back them up manually, before issuing the `nwg-shell-installer -u` command. You may also run the command, and then skip overwriting files. After this, you won't be notified about the upgrade availability any longer.

**Related:**

### nwg-panel v0.7.6

- added grid (launcher) icon;
- CustomButton module: added tooltip text.

### nwg-shell-config v0.3.9

- added `nwg-shell-help` entry point, to get rid of the nwg-wrapper-based help widget. Updated (in nwg-shell v0.2.4) panel presets and the main sway config file come with the help button, and the `[Super]+F1` key binding, to show the keyboard shortcuts help. You may customize the help window behaviour in the shell config utility. The help content may be edited in the `~/.local/share/nwg-shell-config/help.pango` file.
- resolved `autotiling` multiple instances issue, appearing on sway reload.
- added support for the gtklock `userinfo` module.

### nwg-shell-config 0.3.10

- Hot fix for nwg-lock crashing on the "gtklock-userinfo" config key missing.

## nwg-panel 0.7.5 (2022.08.22)

- more icon names updated to be Adawaita conformant #141 by @tewkanz
- fixed SwayWorkspaces crash #142

## nwg-panel 0.7.4 (2022.08.15)

- nwg-panel-config & Clock module: icon names fixed to work with Adwaita icon theme
- added a fix to prevent SwayWorkspaces from crashing on empty floating node.name

## nwg-panel 0.7.3 (2022.07.31)

Clock module: added Calendar window, with the ability to save a simple note for each day.

![image](https://user-images.githubusercontent.com/20579136/182003682-ab3b2e85-69f5-4834-8b65-93c311e19549.png)

Hint: by default, calendar data is stored in the `/home/$USER/.local/share/nwg-panel/calendar.json` file. Use a folder that you sync over the web to access the same calendar on various machines. E.g. you may [install Dropbox](https://wiki.archlinux.org/title/dropbox) and use the `/home/$USER/Dropbox/calendar.json` path.

![image](https://user-images.githubusercontent.com/20579136/182003964-6ca3c1f7-2e0f-4056-8c8e-48b90e9253d2.png)
