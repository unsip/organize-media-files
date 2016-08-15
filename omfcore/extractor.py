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

'''Extract music-file metadata'''

# Standart imports
import pathlib
# Project-specific imports
import mutagen
    

class extractor:
    
    class FileError(RuntimeError):
        pass
    
    metadata = {}

    def __init__(self, filename):
        if not isinstance(filename, str):
            assert False, 'Invalid parameter type.'

        try:
            file = mutagen.File(filename, easy = True)
            wishable_fields = ('album', 'title', 'artist', 'tracknumber')   # Add more fields here

            for field in wishable_fields:
                try:
                    self.metadata[field] = file[field][0]    # mutagen obj is dict-like, but values stored as list of one
                except KeyError:                             # string (dunno why), so we need to refer to the zero element
                    self.metadata[field] = ''

        except (mutagen.MutagenError) as ex:
            raise self.FileError(str(ex))

