# Standart imports
import pathlib
import pytest
import os

# Project-specific imports
from context import make_data_filename
import omfcore

class extractor_tester:

    def setup(self):
        self.na = make_data_filename('non-accessable.flac')
        self.na.chmod(0)

    def teardown(self):
        self.na.chmod(0o644)

    @pytest.mark.parametrize(
        'filename, title, artist, album, tracknumber', [
            ('sample_flac.flac', 'some_title_flac',
                'some_artist_flac', 'some_album_flac', '1'),
            ('sample_mp3.mp3', 'some_title_mp3',
                'some_artist_mp3', 'some_album_mp3', '1'),
            ('sample_ogg.ogg', 'some_title_ogg',
                'some_artist_ogg', 'some_album_ogg', '1')
        ]
    )
    def known_meta_test(self, filename, title, artist, album, tracknumber):
        requested_pattern = '{artist}/{title}/{album}/{tracknumber}'
        meta_fields = omfcore.filter_meta(
            requested_pattern, omfcore.METADATA_FIELDS)

        # Is this method ok? Have to change dir,
        os.chdir(str(pathlib.Path(__file__).parent / 'data'))
        # coz mutagen can't take path in any form
        omfcore.extractor(filename, meta_fields)

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
