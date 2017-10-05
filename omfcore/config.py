# Standard imports
import collections
import configparser
import copy
import pathlib

# Project-specific imports


class config:

    class FileError(RuntimeError):
        pass

    class WryConfigError(RuntimeError):
        pass

    @property
    def pattern(self):
        return self._pattern

    @pattern.setter
    def pattern(self, value):
        # Checking if given pattern is in patterns dict
        if value in self.patterns.keys():  
            self._pattern = self.patterns[value]
        else:
            raise RuntimeError('No usable pattern was found.')

    def __init__(self, filename):
        if isinstance(filename, str):
            filename = pathlib.Path(filename)
        elif not isinstance(filename, pathlib.Path):
            assert False, 'Invalid parameter type. Review ur code.'

        self._pattern = None

        try:
            with filename.open('r') as inp:
                config_string = inp.read()

            # Parse file content
            config = configparser.ConfigParser(
                dict_type=collections.OrderedDict)
            config.read_string(config_string)

            # The result is a list of keys from the only (fake) section
            self.patterns = collections.OrderedDict(config['patterns'])
            default_pattern = dict(config['default pattern'])

            if len(default_pattern) != 1:
                raise KeyError

            if default_pattern['default'] in self.patterns:
                self._pattern = self.patterns[default_pattern['default']]
            else:
                raise RuntimeError(
                    'Invalid default pattern in {}'.format(filename))

        except (FileNotFoundError, PermissionError) as ex:
            raise self.FileError(str(ex))
        except configparser.ParsingError as ex:
            raise self.WryConfigError(str(ex))
        except KeyError:
            emsg = 'Config should contain one default pattern.'
            raise self.WryConfigError(emsg)
        except RuntimeError as ex:
            raise self.WryConfigError(str(ex))

    def merge_from(self, other):
        """ Merge given conf with self. """
        tmp = copy.deepcopy(other.patterns)
        tmp.update(self.patterns)
        self.patterns = tmp
