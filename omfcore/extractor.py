""" Extract music-file metadata. """

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
        """ Fixing metatag data in case of separator occurance. """
        while (os.sep in data):
            data = data.replace(os.sep, '_')

        return data

    def __init__(self, filename, metadata_fields):
        # assert isinstance(filename, pathlib.Path), 'Invalid parameter type.'

        try:
            file = mutagen.File(str(filename), easy=True)

            for field in metadata_fields:
                try:
                    # mutagen obj is dict-like, but values stored as list of one
                    # string (dunno why), so we need to refer to the zero
                    # element
                    fixed_data = self.__fix_metafields(file[field][0])
                    self.metadata[field] = fixed_data
                except KeyError:
                    emsg = ' '.join((
                        '\n',
                        'File:',
                        '{}.\n'.format(filename),
                        'Metatag `{}` is missing.\n'.format(field)
                    ))
                    raise self.FileError(emsg)
                except TypeError:
                    emsg = ' '.join((
                        '\n',
                        'File:',
                        '{}\n'.format(filename),
                        'Invalid filetype to extract meta from.\n'
                    ))
                    raise self.FileError(emsg)

        except (mutagen.MutagenError) as ex:
            raise self.FileError(str(ex))
