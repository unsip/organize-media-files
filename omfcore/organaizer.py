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
import re

# Project-specific imports
from .extractor import extractor

def build_path(metadata, pattern):
    ''' Build path for music file, according to given meta and pattern. '''
    assert isinstance(metadata, dict), 'Invalid argument, should be dict. Review your code.'
    assert isinstance(pattern, str), 'Invalid argument, should be str. Review your code.'

    for field in metadata:
        pattern_to_find = '{' + field + '}'
        pattern = pattern.replace(pattern_to_find, metadata[field])

    return pattern

def dispatch(files_list, pattern):
    ''' Construct list of tuples containing filename's and new path for them. '''
    paths = []
    for file in files_list:
        file = pathlib.Path(file)
        if not file.exists():
            raise RuntimeError      # have to raise it here, coz next step is os.chdir
        
        if file == pathlib.Path('.'):
            raise RuntimeError      # .parent[0] on '.' cause IndexError

        os.chdir(pathlib.Path(__file__).absolute() / file)

        try:
            extractor(str(file.name))
        except (extractor.FileError) as ex:
            raise RuntimeError(str(ex))

        paths.append((file, build_path(extractor.metadata, pattern)))

    return paths

# Dispatch (files_lst, pattern):
#   paths = []
#   for file in files_lst: 
#       valid_path = pathlib.Path.parents[0]
#       filename = pathlib.Path.name
#       
#       if valid_path: 
#           os.chdir(valid_path)
#       extractor(filename)
#       paths.append((file, build_path(extractor.metadata, pattern)))
#
#   return paths
#
# build_path(metadata, pattern) <-- Build path from meta, based on given pattern
# 
# Don't forget stuff:
#   - pathlib.Path.parents[0] raises exception if '.' is given. And '.' is valid path