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

# Standard imports
import argparse
import os
import sys

# Project specific imports
from .config import config

class Application(object):
    def __init__(self):
        parser = argparse.ArgumentParser(description='Organize Media Files')
        parser.add_argument(
            '-d'
          , '--dry-run'
          , action='store_true'
          , help='Do not do the job, just show whats going to be done'
          )
        parser.add_argument(
            '-c'
          , '--config'
          , help='specify an alternative configuration file'
          , metavar='FILE'
          )
        parser.add_argument(
            '-p'
          , '--pattern'
          , metavar='NAME'
          , help='Use given pattern to dispatch incoming files'
          )
        parser.add_argument(
            'file'
          , metavar='INPUT-FILE'
          , nargs='+'
          , help='files to dispatch using a pattern'
          )
        args = parser.parse_args()


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
