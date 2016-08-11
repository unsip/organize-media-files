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

# Project-specific imports
import mutagen

def extractor(filename):
    file = mutagen.File(filename, easy = True)
    wishable_fields = ('album', 'title', 'artist', 'tracknumber')   # Add more fields here
    metadata = {}

    for field in wishable_fields:
        try:
            metadata[field] = file[field][0]    # mutagen obj is dict-like, but values stored as list of one
        except KeyError:                        # string (dunno why), so we need to refer to the zero element
            metadata[field] = ''

    return metadata
