#!/usr/bin/env python3
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
#

from setuptools import setup, find_packages

import omfcore

def readfile(filename):
    with open(filename, encoding='UTF-8') as f:
        return f.read()

setup(
    name               = 'organize-media-files'
  , version            = omfcore.__version__
  , description        = 'Organize Media Files'
  , long_description   = readfile('README.rst')
  , license            = 'GPL-3'
  , url                = 'https://github.com/IsaacMother/organize-media-files'
  , keywords           = ['music collection pranizer']
  , platforms          = ['all']
  , maintainer         = 'Andrey Turbov'
  , maintainer_email   = 'andrey.turbov@gmail.com'
  , data_files         = [('/etc/.omfrc/', ['contrib/user.conf']),
                          ('/etc/.omfrc/', ['contrib/system.conf'])
      ]
  , entry_points       = {
        'console_scripts': [
            'omf = omfcore.cli:main'
          ]
      }
    # NOTE Take a look to http://setuptools.readthedocs.io/en/latest/setuptools.html#dynamic-discovery-of-services-and-plugins
    # for possible future extensions
  , packages           = find_packages(exclude=['test'])
  , classifiers        = [
        'Development Status :: 4 - Beta'
      , 'Environment :: Console'
      , 'Intended Audience :: Developers'
      , 'License :: Other/Proprietary License'
      , 'Natural Language :: English'
      , 'Operating System :: OS Independent'
      , 'Programming Language :: Python :: 3.5'
      , 'Topic :: Multimedia :: Sound/Audio'
      , 'Topic :: Utilities'
      ]
  , install_requires   = ['mutagen']
  , test_suite         = 'test'
  , tests_require      = ['pytest']
  , zip_safe           = True
  )
