#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Organize Media Files
#
# Copyright (c) 2016 Andrey Turbov <andrey.turbov@gmail.com>
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
import pathlib
import sys

# Project-specific imports
from .config import config
from .extractor import extractor
from .organaizer import dispatch, action_run, dry_run

SYSTEM_CONFIG = '/etc/.omfrc/system.conf'
USER_CONF = '/etc/.omfrc/user.conf'

class Application(object):

    def __init__(self):
        parser = argparse.ArgumentParser(description='Organize Media Files')
        parser.add_argument(
            '-d'
          , '--dry-run'
          , action='store_true'
          , default=False
          , help='Do not do the job, just show whats going to be done'
          )
        parser.add_argument(
            '-c'
          , '--config'
          , help='specify an alternative configuration file'
          , metavar='FILE'
          )
        parser.add_argument(
            '-f'
          , '--force'
          , action='store_true'
          , default=False
          , help='ignore inconsistencies or/and overwrite files'
          )
        parser.add_argument(
            '-p'
          , '--pattern'
          , metavar='PATTERN-NAME'
          , help='Use given pattern to dispatch incoming files'
          )
        parser.add_argument(
            'file'
          , metavar='INPUT-FILE'
          , nargs='+'
          , help='files to dispatch using a pattern'
          )
        args = parser.parse_args()

        #print('args={}'.format(repr(args)))

        if args.config is not None:
            cfg_file = pathlib.Path(args.config)
            self.config = config(cfg_file)
        else:
            # Check if system-wide config is here
            system_cfg_file = pathlib.Path(SYSTEM_CONFIG)
            system_conf = None
            if system_cfg_file.exists():
                system_conf = config(system_cfg_file)

            # Check user config
            user_cfg_file = pathlib.Path(pathlib.Path.home() / USER_CONF)

            user_conf = None
            if user_cfg_file.exists():
                user_conf = config(user_cfg_file)

            if system_conf and user_conf:
                self.config = user_conf
                self.config.merge_from(system_conf)
            elif system_conf:
                self.config = system_conf
            elif user_conf:
                self.config = user_conf
            else:
                raise RuntimeError('No config file has been found/given.')

        # Sanity check
        assert self.config is not None

        # Add other parameters from CLI
        self.config.dry_run = args.dry_run
        self.config.files = list(args.file)
        if args.pattern: self.config.pattern = args.pattern
        self.config.force = args.force

        # Check for valid config
        self.config.validate()

    def run(self):
        paths = dispatch(self.config.files, self.config.pattern, self.config.force)

        #print(repr(paths))

        if self.config.dry_run:
            dry_run(paths, self.config.force)
        else:
            action_run(paths, self.config.force)

def main():
    try:
        a = Application()
        a.run()
    except KeyboardInterrupt:
        sys.exit(1)
    except RuntimeError as ex:
        print('*** Error: {}'.format(ex))
        sys.exit(1)
    sys.exit(0)