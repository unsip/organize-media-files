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

''' Unit tests for path-organization functions. '''

# Standart imports
import os
import pathlib
import pytest

# Project-specific imports
import omfcore
from context import make_data_filename
      
class organaize_tester:

    def setup(self):
      pass

    @pytest.mark.parametrize(
        'file'
      , [
            (make_data_filename('sample_mp3.mp3'))
          , (make_data_filename('sample_flac.flac'))
          , (make_data_filename('sample_ogg.ogg'))
        ]
      )
    def build_path_test(self, file):
        pattern = '/storage/music/{artist}/{album}/{tracknumber}_{title}'
        expected = '/storage/music/some_artist_{0}/some_album_{0}/1_some_title_{0}'.format(file.suffix[1:])
        
        meta_fields = omfcore.filter_meta(pattern, omfcore.METADATA_FIELDS)

        os.chdir(str(file.parents[0]))
        mutagen_obj = omfcore.extractor(str(file.name), meta_fields)
        output = omfcore.build_path(mutagen_obj.metadata, pattern)

        assert output == expected

    @pytest.mark.parametrize(
        'files_lst, exception'
      , [
            ([pathlib.Path('.')], RuntimeError)
          , ([pathlib.Path('non/existing/path')], RuntimeError)
        ]
      )
    def dispatch_test(self, files_lst, exception):
        pattern = '/storage/music/{artist}/{album}/{tracknumber}_{title}'

        with pytest.raises(exception) as ex:
            omfcore.dispatch(files_lst, pattern, False)

    @pytest.mark.parametrize(
        'pattern, expected_metafields'
      , [
            (
              '/storage/music/{artist}/{album}/{tracknumber}_{title}'
              , ('artist', 'album', 'tracknumber', 'title')
            )
          , (
              '/home/david/{{badstuff}}/{wrong}}/{{{title}}/{genre}'
              , ('title', 'genre')
            )
        ]
      )
    def filter_test(self, pattern, expected_metafields):
        result = omfcore.filter_meta(pattern, omfcore.METADATA_FIELDS)
        assert result == set(expected_metafields)