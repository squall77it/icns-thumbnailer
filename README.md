ICNS Thumbnailer
================

A thumbnailer for Mac OS X icon files in Gnome 3

Allows Nautilus to generate thumbnail previews for `.icns`  files!

It can also be used as a stand-alone converter from `icns` to `png` :)

Requirements
------------

- Pyton (tested in 2.7)
- gir bindings for `GLib` and `GdkPixbuf`

The above are already installed by default in any Gnome-based distro, but if somehow you don't, the command for Debian-like distros (like Ubuntu/Mint) is:

`sudo apt-get python gir1.2-gdkpixbuf-2.0 gir1.2-glib-2.0`

Install
-------

Clone the repository and run:

`./install`

By default it install files to `~/.local/share` tree, for your user only. For a system-wide install, available to all users, just run as root:

`sudo ./install`

It will install files to `/usr/local` tree.

`install --help` is also available, for those who care.

Uninstall
---------

For your user: `./install --uninstall`

For system-wise: `sudo ./install --uninstall`

Usage as thumbnailer
--------------------

After install, just restart Nautilus (or log out and back in to be sure). After that, Nautilus will *automagically* generate shiny new thumbnails for your `icns` files. Just browse them and enjoy your icon previews in all their glory.

Usage as a stand-alone converter
--------------------------------

Assuming the install dir is in your `$PATH` (and for user-installs, `~/.local/bin` usually is **not**), you can use the thumbnailer as a converter to `PNG`. The syntax is:

`icns-thumbnailer inputfile outputfile [size]`

Where:

- `inputfile` must be an existing, readable, *locally-available* file. URIs, like `file://`, `smb://`, `http://` etc, are *not* supported, but could be in the future. Remote files that are locally mounted, accessible via `/some/path`, are fine. And, of course, it must be a valid `icns` file. (Well, actually *any* image file natively  supported by `GdkPixbuf` will work, but don't tell anyone!). For multi-image icons, as most are, it the largest image will be converted/resized.

- `outputfile` must be a writable file path. If it already exists, it will be overwritten. No URIs either. Output format will be `PNG`. (Yes, even if you name it `somethingelse.jpg`, sorry)

- `size` is an optional *maximum* image size, in pixels. It will shrink (but never enlarge) the image by setting the largest of width or height to `size`, and ajusting the other to keep original aspect ratio. If `size` is missing or `0`, it will convert the image without resizing it.

Contributing
------------

Patches are welcome! Fork, hack, request pull! Here is my current to-do list:

- **Support URIs for local files**: `GIO`'s `g_file_new_for_uri()` and `g_file_get_path()` might help converting from `file://` to a local path (if any) to feed `GdkPixbuf`

- **Support remote files**: a bit trickier, since currently `GdkPixbuf` does not support incremental load for `icns` files, which rules out any input via stream. A possible approach would be to use  `outputfile` as a temp file to save `inputfile`, feed it to `GdkPixbuf`, and make sure it will be closed before saving the resized output.

- **Proper command-line argument parse** via `argparse` module

- **Improve error handling and reporting**: consistent Exception bubbling, finer-grain usage of `GLib.GError`, `logging` module for console verbosity, including `-q|--quiet` for `.thumbnailer` usage, consistent exit status.

Also, about the above, please help promoting the following related bugs:

https://bugzilla.gnome.org/show_bug.cgi?id=531059

https://bugzilla.gnome.org/show_bug.cgi?id=469912

https://bugzilla.gnome.org/show_bug.cgi?id=629474

And the most important one:

https://bugzilla.gnome.org/show_bug.cgi?id=699414

Written by
----------

Rodrigo Silva (MestreLion) <linux@rodrigosilva.com>

Licenses and Copyright
----------------------

Copyright (C) 2013 Rodrigo Silva (MestreLion) <linux@rodrigosilva.com>.

License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.

This is free software: you are free to change and redistribute it.

There is NO WARRANTY, to the extent permitted by law.
