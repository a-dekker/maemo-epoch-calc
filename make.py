#!/usr/bin/python
# -*- coding: utf-8 -*-
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation; version 2 only.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
import pypackager
import os


if __name__ == "__main__":
    try:
        os.chdir(os.path.dirname(sys.argv[0]))
    except:
        pass

    p = pypackager.PyPackager("epoch-calc")
    p.version = '0.0.1'
    p.buildversion = '4'
    p.display_name = 'epoch-calc'
    p.description = "Assistant for calculating Unix time"
    p.author = "Arno Dekker"
    p.maintainer = "Arno Dekker"
    p.email = "mymail@gmail.com"
    p.depends = "python2.5,python2.5-qt4-gui,python2.5-qt4-core,python2.5-qt4-maemo5,python-pyside.qtgui,python-pyside.qtmaemo5,python-pyside.qtcore"
    p.suggests = ""
    p.section = "user/utilities"
    p.arch = "armel"
    p.urgency = "low"
    p.bugtracker = 'http://talk.maemo.org/showthread.php?t=91713'
    p.changelog = changelog = "* Initial Release"
    p.distribution = "fremantle"
    p.repository = "extras-devel"
    p.icon = '/home/user/sources/epoch-calc/src/usr/share/icons/hicolor/64x64/apps/epoch-calc.png'

    dir_name = "src"
    for root, dirs, files in os.walk(dir_name):
        real_dir = root[len(dir_name):]
        fake_file = []
        for f in files:
            fake_file.append(root + os.sep + f + "|" + f)
        if len(fake_file) > 0:
            p[real_dir] = fake_file
    print p

    # p["/usr/lib/python2.5/site-packages"] = files

    p.postinstall = """#!/bin/sh
        chmod +x /opt/epoch-calc/epoch-calc
"""

    p.changelog = """
* fixed: small periode in am/pm indication was wrong
"""

# print p.generate(build_binary=False,build_src=True)
print p.generate(build_binary=True,build_src=True)
