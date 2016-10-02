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

''' Path-organization functions. '''

# Standart imports
import os
import pathlib
import shutil

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
        file = file.expanduser()
        
        if file == pathlib.Path('.'):
            raise RuntimeError('No such file or directory.')      # .parent[0] on '.' cause IndexError

        try:
            extractor(str(file), METADATA_FIELDS)
        except (extractor.FileError) as ex:
            if not force:
                raise RuntimeError(str(ex))

        # Building path and expanding '~' symbols in it.
        complete_path = pathlib.Path(build_path(extractor.metadata, pattern))
        complete_path = complete_path.expanduser()

        paths.append((file, complete_path))

    return paths

def dry_run(paths, force):
    ''' Displays behaviour in a particular case. '''
    for pair in paths:
        if pair[1].exists() and not force:
            print('{}:'.format(pair[0].name))
            
            strg = ' '.join((
                    '   '
                  , 'Warning, file {} already exists'.format(str(pair[1].name))
                  , 'and won\'t be processed,' 
                  , 'unless --force specified.'
                ))
            print(strg)
        else:
            print('    Moving {0} to {1}'.format(pair[0], pair[1]))

def action_run(paths, force):
    ''' Core process of moving files. '''
    for pair in paths:
        if pair[1].exists() and not force:
            raise RuntimeError('Same file {} exists and --force not specified'.format(str(pair[0])))

    for pair in paths:
        try:
            if pair[1].parents[0] != pathlib.Path('.') and not pair[1].parents[0].exists():
                pair[1].parents[0].mkdir(parents=True)
            
            shutil.move(str(pair[0]), str(pair[1]))
        except (OSError) as ex:
            raise RuntimeError(ex)