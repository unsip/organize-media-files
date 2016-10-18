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
import collections
import configparser
import copy
import pathlib


# Project-specific imports

class config:

    class FileError(RuntimeError):
        pass

    class WryConfigError(RuntimeError):
        pass

    dry_run = False                                         # Option to indicate `dry-run`                                        # Name of pattern to use
    files = None                                            # List of files to process
    force = False                                           # Ignore inconsistencies

    @property
    def pattern(self):
        return self._pattern

    @pattern.setter
    def pattern(self, value):
        if value in self.patterns.keys():   # Checking if given pattern is in patterns dict
            self._pattern = self.patterns[value]
        else:
            raise RuntimeError('No usable pattern was found.')

    def __init__(self, filename):
        if isinstance(filename, str):
            filename = pathlib.Path(filename)
        elif not isinstance(filename, pathlib.Path):
            assert False, 'Invalid parameter type. Review ur code.'

        self._pattern = None

        try:
            with filename.open('r') as inp:
                config_string = inp.read()
            
            # Parse file content
            config = configparser.ConfigParser(dict_type=collections.OrderedDict)
            config.read_string(config_string)

            # The result is a list of keys from the only (fake) section
            self.patterns = collections.OrderedDict(config['patterns'])
            default_pattern = dict(config['default pattern'])
            
            if len(default_pattern) != 1: raise KeyError
            
            if default_pattern['default'] in self.patterns:
                self._pattern = self.patterns[default_pattern['default']]
            else:
                raise RuntimeError('Invalid default pattern in {}'.format(filename))

        except (FileNotFoundError, PermissionError) as ex:
            raise self.FileError(str(ex))
        except configparser.ParsingError as ex:
            raise self.WryConfigError(str(ex))
        except KeyError:
            raise self.WryConfigError('Config should contain one default pattern.')
        except RuntimeError as ex:
            raise self.WryConfigError(str(ex))

    def merge_from(self, other):
        '''Merge given conf with self. '''
        tmp = copy.deepcopy(other.patterns)
        tmp.update(self.patterns)
        self.patterns = tmp

    def validate(self):
        '''Make sure that .conf's are valid to work with.'''
        assert self._pattern is not None, 'Set some `pattern` before validate.'
        assert isinstance(self.files, list)
        assert len(self.files)