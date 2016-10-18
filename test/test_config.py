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

''' Unit tests for `config` module '''

# Standard imports
import pathlib
import pytest

# Project-specific imports
import omfcore
from context import make_data_filename

class config_tester:

    def setup(self):
        self.na = make_data_filename('non_accessible.conf')
        self.na.chmod(0)

    def teardown(self):
        self.na.chmod(0o644)

    @pytest.mark.parametrize(
        'filename, exception_type'
      , [
            ('non_existing.conf', omfcore.config.FileError)
          , (make_data_filename('non_accessible.conf'), omfcore.config.FileError)
          , (make_data_filename('wry.conf'), omfcore.config.WryConfigError)
          , (make_data_filename('wry_1.conf'), omfcore.config.WryConfigError)
          , (make_data_filename('wry_2.conf'), omfcore.config.WryConfigError)
          , (make_data_filename('wry_3.conf'), omfcore.config.WryConfigError)
          , (make_data_filename('wry_4.conf'), omfcore.config.WryConfigError)
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