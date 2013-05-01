#!/usr/bin/env python
#
# icns_thumbnailer.py - A Gnome 3 thumbnailer for Mac OSX 'icns' icon files
#
#    Copyright (C) 2013 Rodrigo Silva (MestreLion) <linux@rodrigosilva.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/gpl>.

import sys
from gi.repository import GdkPixbuf, GLib

def make_thumbnail(inputname, outputname, size=0):
    try:
        # new_from_file_at_size() does not work, requires incremental loader
        pixbuf = GdkPixbuf.Pixbuf.new_from_file(inputname)
        if size:
            width, height = pixbuf.get_width(), pixbuf.get_height()
            if width > height:
                if width > size:
                    height = height * size / width
                    width  = size
            else:
                if height > size:
                    width  = width * size / height
                    height = size

            scaled = GdkPixbuf.Pixbuf.scale_simple(pixbuf, width, height,
                                                   GdkPixbuf.InterpType.BILINEAR)
        else:
            scaled = pixbuf

        scaled.savev(outputname, 'png', [], [])

    except GLib.GError as e:
        sys.stderr.write("%s:%d: %s\n" % (e.domain, e.code, e))
        return e.code

def main(argv):
    try:
        args = argv[1], argv[2], int((argv[3:4] or [0])[0])
        if len(argv) > 4: raise IndexError
    except (ValueError, IndexError):
        sys.stderr.write("Usage: %s inputfile outputfile [size]\n" % argv[0])
        return 1

    return make_thumbnail(*args)

if __name__ == '__main__':
    sys.exit(main(sys.argv))