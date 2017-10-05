# Standard imports
import pathlib
import pytest

# Project-specific imports
from context import make_data_filename
import omfcore

class config_tester:

    def setup(self):
        self.na = make_data_filename('non_accessible.conf')
        self.na.chmod(0)

    def teardown(self):
        self.na.chmod(0o644)

    @pytest.mark.parametrize(
        'filename, exception_type', [
            ('non_existing.conf', omfcore.config.FileError),
            (make_data_filename('non_accessible.conf'), omfcore.config.FileError),
            (make_data_filename('wry.conf'), omfcore.config.WryConfigError),
            (make_data_filename('wry_1.conf'), omfcore.config.WryConfigError),
            (make_data_filename('wry_2.conf'), omfcore.config.WryConfigError),
            (make_data_filename('wry_3.conf'), omfcore.config.WryConfigError),
            (make_data_filename('wry_4.conf'), omfcore.config.WryConfigError)
        ]
    )
    def open_config_test(self, filename, exception_type):
        with pytest.raises(exception_type) as ex:
            omfcore.config(filename)

    def config_test(self):
        system_conf = omfcore.config(make_data_filename('system.conf'))
        user_conf = omfcore.config(make_data_filename('user.conf'))

        assert system_conf.pattern == 'satu'
        assert isinstance(system_conf.patterns, dict)
        assert len(system_conf.patterns) == 2

        assert user_conf.pattern == 'dua'
        assert isinstance(user_conf.patterns, dict)
        assert len(user_conf.patterns) == 2

        user_conf.merge_from(system_conf)

        assert system_conf.pattern == 'satu'
        assert len(system_conf.patterns) == 2
        assert system_conf.patterns['one'] == 'satu'
        assert system_conf.patterns['two'] == 'two'

        assert user_conf.pattern == 'dua'
        assert len(user_conf.patterns) == 3
        assert user_conf.patterns['one'] == 'satu'
        assert user_conf.patterns['two'] == 'dua'
        assert user_conf.patterns['three'] == 'tiga'
