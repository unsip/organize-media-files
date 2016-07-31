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

''' Unit tests for `config` module '''

# Standard imports
import pytest

# Project specific imports
import omfcore
from context import make_data_filename

class config_tester:

    def setup(self):
        self.system_conf = omfcore.config(make_data_filename('system.conf'))
        self.user_conf = omfcore.config(make_data_filename('user.conf'))


    def config_test(self):
        assert isinstance(self.system_conf.patterns, dict)
        assert len(self.system_conf.patterns) == 2
        assert isinstance(self.user_conf.patterns, dict)
        assert len(self.user_conf.patterns) == 2

        self.user_conf.merge_from(self.system_conf)

        assert len(self.system_conf.patterns) == 2
        assert self.system_conf.patterns['one'] == 'satu'
        assert self.system_conf.patterns['two'] == 'two'

        assert len(self.user_conf.patterns) == 3
        assert self.user_conf.patterns['one'] == 'satu'
        assert self.user_conf.patterns['two'] == 'dua'
        assert self.user_conf.patterns['three'] == 'tiga'
