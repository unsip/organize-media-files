from setuptools import setup, find_packages
from glob import glob
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
  , data_files         = [('/etc/omf.conf', 'contrib/system.conf'),
                          ('omf_example', glob('example/*'))
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
