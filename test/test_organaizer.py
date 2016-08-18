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
        'files_lst'
      , [
            ()
          , ()
          , ()
        ]
      )
    def dispatch_test(self, files_lst):
        pass

    @pytest.mark.parametrize(
        'filepath'
      , [
            (make_data_filename('sample_mp3.mp3'))
          , (pathlib.Path(os.getcwd()).parent / 'README.md')
          , (pathlib.Path(os.getcwd()) / 'test_config.py')
        ]
      )
    def validate_path_test(self, filepath):
        valid_path, filename = omfcore.organaizer.validate_path(str(filepath))
        assert valid_path / filename == str(filepath)

    @pytest.mark.parametrize(
        'metadata'
      , [
            ()
          , ()
          , ()
        ]
      )
    def build_path_test(self, metadata):
        pass

    def path_checker_test(self):
        pass


# Dispatch (files_lst, pattern):
#   paths = []
#   for file in files_lst: 
#       valid_path, filename = validate_path(file)
#       
#       if valid_path: 
#           os.chdir(valid_path)
#       extractor(filename)
#       paths.append((file, build_path(extractor.metadata, pattern)))
#
#   return paths
#
# validate_path(file) <--- Would return valid_path and filename 
# build_path(metadata, pattern) <-- Build path from meta, based on given pattern
# 
# Questions:
# - What about imports like `from .config import config`, would it autoimport inner-used modules?
# - How to currectly organize dispatching, as whole new class?
# - How to organize class, with private methods (such as validate_path(file))?