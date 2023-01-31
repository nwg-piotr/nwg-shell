#!/usr/bin/env python3

"""
nwg-shell installer GUI
Repository: https://github.com/nwg-piotr/nwg-shell
Project site: https://nwg-piotr.github.io/nwg-shell
Author's email: nwg.piotr@gmail.com
Copyright (c) 2023 Piotr Miller
License: MIT
"""

from nwg_shell.tools import *
from nwg_shell.__about__ import __version__
import gi

gi.require_version('Gdk', '3.0')
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib

dir_name = os.path.dirname(__file__)

voc = {}
apps = {
    "file-manager": "thunar",
    "text-editor": "mousepad",
    "web-browser": "chromium"
}
browsers = {
    "brave": "brave --enable-features=UseOzonePlatform --ozone-platform=wayland",
    "chromium": "chromium --enable-features=UseOzonePlatform --ozone-platform=wayland",
    "google-chrome-stable": "google-chrome-stable --enable-features=UseOzonePlatform --ozone-platform=wayland",
    "epiphany": "epiphany",
    "falkon": "falkon",
    "firefox": "MOZ_ENABLE_WAYLAND=1 firefox",
    "konqueror": "konqueror",
    "midori": "midori",
    "opera": "opera",
    "qutebrowser": "qutebrowser",
    "seamonkey": "seamonkey",
    "surf": "surf",
    "vivaldi-stable": "vivaldi-stable --enable-features=UseOzonePlatform --ozone-platform=wayland",
}


def load_vocabulary():
    global voc
    # basic vocabulary (for en_US)
    voc = load_json(os.path.join(dir_name, "langs", "en_US.json"))
    if not voc:
        eprint("Failed loading vocabulary")
        sys.exit(1)

    lang = os.getenv("LANG").split(".")[0]
    # translate if necessary
    if lang != "en_US":
        loc_file = os.path.join(dir_name, "langs", "{}.json".format(lang))
        if os.path.isfile(loc_file):
            # localized vocabulary
            loc = load_json(loc_file)
            if not loc:
                eprint("Failed loading translation into '{}'".format(lang))
            else:
                for key in loc:
                    voc[key] = loc[key]


def main():
    GLib.set_prgname('nwg-shell')
    load_vocabulary()

    win = Gtk.Window.new(Gtk.WindowType.TOPLEVEL)
    win.connect('destroy', Gtk.main_quit)

    box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 12)
    box.set_property("margin", 12)
    win.add(box)

    hbox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 0)
    box.pack_start(hbox, False, False, 0)
    img = Gtk.Image.new_from_icon_name("nwg-shell", Gtk.IconSize.DIALOG)
    box.pack_start(img, False, False, 0)

    hbox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 0)
    box.pack_start(hbox, False, False, 0)
    lbl = Gtk.Label.new("nwg-shell v{}".format(__version__))
    hbox.pack_start(lbl, True, True, 0)

    hbox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 0)
    box.pack_start(hbox, False, False, 0)
    lbl = Gtk.Label.new(voc["welcome"])
    hbox.pack_start(lbl, True, True, 0)

    hbox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 0)
    box.pack_start(hbox, False, False, 0)
    lbl = Gtk.Label.new("{}\n{}".format(voc["status-0"], voc["status-1"]))
    lbl.set_property("justify", Gtk.Justification.CENTER)
    hbox.pack_start(lbl, True, True, 0)

    hbox = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 0)
    box.pack_start(hbox, False, False, 0)
    grid = Gtk.Grid()
    grid.set_column_spacing(12)
    grid.set_row_spacing(12)
    grid.set_property("margin", 12)
    hbox.pack_start(grid, True, False, 0)
    lbl = Gtk.Label.new("{}:".format(voc["file-manager"]))
    lbl.set_property("halign", Gtk.Align.END)
    grid.attach(lbl, 0, 0, 1, 1)

    combo_fm = Gtk.ComboBoxText()
    for item in ["caja", "dolphin", "nautilus", "nemo", "pcmanfm", "thunar"]:
        combo_fm.append(item, item)
    combo_fm.set_active_id("thunar")
    grid.attach(combo_fm, 1, 0, 1, 1)

    lbl = Gtk.Label.new("{}:".format(voc["text-editor"]))
    lbl.set_property("halign", Gtk.Align.END)
    grid.attach(lbl, 0, 1, 1, 1)

    combo_fm = Gtk.ComboBoxText()
    for item in ["atom", "emacs", "gedit", "geany", "kate", "mousepad", "vim"]:
        combo_fm.append(item, item)
    combo_fm.set_active_id("mousepad")
    grid.attach(combo_fm, 1, 1, 1, 1)

    lbl = Gtk.Label.new("{}:".format(voc["web-browser"]))
    lbl.set_property("halign", Gtk.Align.END)
    grid.attach(lbl, 0, 2, 1, 1)

    combo_fm = Gtk.ComboBoxText()
    for item in ["brave", "chromium", "google-chrome-stable", "epiphany", "falkon", "firefox", "konqueror", "midori",
                 "opera", "qutebrowser", "seamonkey", "surf", "vivaldi-stable"]:
        combo_fm.append(item, item)
    combo_fm.set_active_id("chromium")
    grid.attach(combo_fm, 1, 2, 1, 1)

    win.show_all()
    Gtk.main()


if __name__ == '__main__':
    sys.exit(main())
