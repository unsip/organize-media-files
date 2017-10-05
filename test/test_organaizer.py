# Standart imports
import os
import pathlib
import pytest

# Project-specific imports
from context import make_data_filename
import omfcore

class organaize_tester:

    def setup(self):
        pass

    @pytest.mark.parametrize(
        'file', [
            (make_data_filename('sample_mp3.mp3')),
            (make_data_filename('sample_flac.flac')),
            (make_data_filename('sample_ogg.ogg'))
        ]
    )
    def build_path_test(self, file):
        pattern = '/storage/music/{artist}/{album}/{tracknumber}_{title}'
        expected = '/storage/music/some_artist_{0}/some_album_{0}/1_some_title_{0}.{0}'.format(
            file.suffix[1:])

        meta_fields = omfcore.filter_meta(pattern, omfcore.METADATA_FIELDS)

        os.chdir(str(file.parents[0]))
        mutagen_obj = omfcore.extractor(str(file.name), meta_fields)
        output = omfcore.build_path(mutagen_obj.metadata, file.suffix, pattern)

        assert output == expected

    @pytest.mark.parametrize(
        'files_lst, exception', [
            ([pathlib.Path('.')], RuntimeError),
            ([pathlib.Path('non/existing/path')], RuntimeError)
        ]
    )
    def dispatch_test(self, files_lst, exception):
        pattern = '/storage/music/{artist}/{album}/{tracknumber}_{title}'

        with pytest.raises(exception) as ex:
            omfcore.dispatch(files_lst, pattern, False)

    @pytest.mark.parametrize(
        'pattern, expected_metafields', [
            ('/storage/music/{artist}/{album}/{tracknumber}_{title}',
                ('artist', 'album', 'tracknumber', 'title')
            ),
            ('/home/david/{{badstuff}}/{wrong}}/{{{title}}/{genre}',
                ('title', 'genre')
            )
        ]
    )
    def filter_test(self, pattern, expected_metafields):
        result = omfcore.filter_meta(pattern, omfcore.METADATA_FIELDS)
        assert result == set(expected_metafields)
