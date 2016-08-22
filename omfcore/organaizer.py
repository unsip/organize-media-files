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

''' Path-organization functions. '''

# Standart imports
import os
import pathlib

# Project-specific imports
from .extractor import extractor
from .core_varaibles import METADATA_FIELDS

def build_path(metadata, pattern):
    ''' Build path for music file, according to given meta and pattern. '''
    assert isinstance(metadata, dict), 'Invalid argument, should be dict. Review your code.'
    assert isinstance(pattern, str), 'Invalid argument, should be str. Review your code.'

    for field in metadata:
        pattern_to_find = '{' + field + '}'
        pattern = pattern.replace(pattern_to_find, metadata[field])

    return pattern

def dispatch(files_list, pattern, force):
    ''' Construct list of tuples containing filename's and new path for them. '''
    paths = []

    for file in files_list:
        file = pathlib.Path(file)
        if file == pathlib.Path('.'):
            raise RuntimeError('No such file or directory.')      # .parent[0] on '.' cause IndexError

        try:
            extractor(str(file), METADATA_FIELDS)
        except (extractor.FileError) as ex:
            if not force:
                raise RuntimeError(str(ex))

        paths.append((file, pathlib.Path(build_path(extractor.metadata, pattern))))

    return paths