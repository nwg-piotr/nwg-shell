# Recent updates

## nwg-shell 0.3.0 (2022.09.09)

This release brings the graphical updater, that replaces the former `nwg-shell-installer -u` CLI command. You'll be notified about shell updates via system notifications with 'Update' and 'Later' actions. If you decide to update later, you may open the shell config utility, and use the 'Updates' button. It will show the number of pending updates, if any. 

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
