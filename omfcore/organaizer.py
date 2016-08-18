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
import pathlib

# Project-specific imports
from .extractor import extractor

def validate_path(file_path):
    ''' Prepare path for futher using by mutagen by separatating full-path into path + file. '''
    pass

def build_path(metadata, pattern):
    ''' Build path for music file, according to given meta and pattern. '''
    pass

def path_checker(filename, path):
    ''' Check if file with the same name exists in given path. '''
    pass

def dispatch(files_list, pattern):
    ''' Construct list of tuples containing filename's and new path for them. '''
    pass