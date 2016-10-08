# -*- coding: utf-8 -*-
#
# Organize Media Files
#-
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

'''Extract music-file metadata'''

# Standart imports
import os
import pathlib
# Project-specific imports
import mutagen


class extractor:

    class FileError(RuntimeError):
        pass

    metadata = {}

    def __fix_metafields(self, data):
        ''' Fixing metatag data in case of separator occurance.'''
        while (os.sep in data):
            data = data.replace(os.sep, '_')

        return data

    def __init__(self, filename, metadata_fields):
        if not isinstance(filename, str):
            assert False, 'Invalid parameter type.'

        try:
            file = mutagen.File(filename, easy = True)

            for field in metadata_fields:
                try:
                    # mutagen obj is dict-like, but values stored as list of one
                    # string (dunno why), so we need to refer to the zero element
                    fixed_data = self.__fix_metafields(file[field][0])
                    self.metadata[field] = fixed_data
                except KeyError:                             
                    strg = ' '.join((
                            '\n'
                          , 'File:'
                          , '{}.\n'.format(filename)
                          , 'Metatag `{}` is missing.\n'.format(field)
                        ))
                    raise self.FileError(strg)
                except TypeError:
                    strg = ' '.join((
                        '\n'
                      , 'File:'
                      , '{}\n'.format(filename)
                      , 'Invalid filetype to extract meta from.\n'
                    ))
                    raise self.FileError(strg)

        except (mutagen.MutagenError) as ex:
            raise self.FileError(str(ex))


