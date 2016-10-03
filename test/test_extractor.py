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

'''Unittests for metadata extracting.'''

# Standart imports
import pathlib
import pytest
import os

# Project-specific imports
import omfcore
from context import make_data_filename

class extractor_tester:
    
    def setup(self):
        self.na = make_data_filename('non-accessable.flac')
        self.na.chmod(0)

    def teardown(self):
        self.na.chmod(0o644)

    @pytest.mark.parametrize(
        'filename, title, artist, album, tracknumber'
      , [
            ('sample_flac.flac', 'some_title_flac', 'some_artist_flac', 'some_album_flac', '1')
          , ('sample_mp3.mp3', 'some_title_mp3', 'some_artist_mp3', 'some_album_mp3', '1')
          , ('sample_ogg.ogg', 'some_title_ogg', 'some_artist_ogg', 'some_album_ogg', '1')
        ]
      )
    def known_meta_test(self, filename, title, artist, album, tracknumber):
        requested_pattern = '{artist}/{title}/{album}/{tracknumber}'
        meta_fields = omfcore.filter_meta(requested_pattern, omfcore.METADATA_FIELDS)

        os.chdir(str(pathlib.Path(__file__).parent / 'data'))   # Is this method ok? Have to change dir,
        omfcore.extractor(filename, meta_fields)    # coz mutagen can't take path in any form
        
        assert title == omfcore.extractor.metadata['title']
        assert artist == omfcore.extractor.metadata['artist']
        assert album == omfcore.extractor.metadata['album']
        assert tracknumber == omfcore.extractor.metadata['tracknumber']

    def na_test(self):
        os.chdir(str(pathlib.Path(__file__).parent / 'data'))

        # Not using pytest decorator coz was getting TypeError, dunno why
        with pytest.raises(omfcore.extractor.FileError) as ex:
            omfcore.extractor('non-accessable.flac', omfcore.METADATA_FIELDS)

        with pytest.raises(omfcore.extractor.FileError) as ex:
            omfcore.extractor('non-existing.flac', omfcore.METADATA_FIELDS)