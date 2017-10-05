""" Helper functions for tests. """

# Standard imports
import pathlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

_data_dir = pathlib.Path(__file__).parent / 'data'


def make_data_filename(filename):
    return _data_dir / filename


def data_dir_base():
    return _data_dir
