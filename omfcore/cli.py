#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Organize Media Files
#
# Copyright (c) 2016 Alex Turbov <i.zaufi@gmail.com>
#
# Organize Media Files is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Organize Media Files is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.


import argparse
import os
import sys

class Application(object):
    def __init__(self):
        pass

    def run(self):
        pass


def main():
    try:
        a = Application()
        a.run()
    except KeyboardInterrupt:
        sys.exit(1)
    except RuntimeError as ex:
        print('Error: {}'.format(ex))
        sys.exit(1)
    sys.exit(0)
