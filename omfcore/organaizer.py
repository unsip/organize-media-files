""" Path-organization functions. """

# Standart imports
import collections
import itertools
import os
import pathlib
import shutil

# Project-specific imports
from .extractor import extractor
from .core_varaibles import METADATA_FIELDS

src_dst_pair = collections.namedtuple('src_dst_pair', ['src', 'dst'])

def build_path(metadata, suffix, pattern):
    """ Build path for music file, according to given meta and pattern. """
    assert isinstance(metadata, dict), \
        'Invalid argument, should be dict. Review your code.'
    assert isinstance(pattern, str), \
        'Invalid argument, should be str. Review your code.'

    for field in metadata:
        pattern_to_find = '{' + field + '}'
        pattern = pattern.replace(pattern_to_find, metadata[field])
    
    pattern = pattern + suffix

    return pattern


def dispatch(files_list, pattern, force):
    """ Construct list of tuples containing filename's and new path for them. """
    paths = []

    for src in files_list:
        src = pathlib.Path(src)
        src = src.expanduser()

        if not src.exists():
            raise RuntimeError('No such file.')

        metafields = filter_meta(pattern, METADATA_FIELDS)

        try:
            extractor(src, metafields)
        except (extractor.FileError) as ex:
            if not force:
                raise RuntimeError(str(ex))
            else:
                # Use click.echo 
                print(str(ex))
                continue
        # Building path and expanding '~' symbols in it.
        dst = pathlib.Path(
                build_path(extractor.metadata, src.suffix, pattern))
        dst = dst.expanduser()

        paths.append(src_dst_pair(
            src.absolute().resolve(),
            dst.absolute().resolve()))

    return paths

def apply_move(paths, force, dry_run):
    """ Core process of moving files. """
    assert isinstance(paths, list)
    assert len(paths)

    not_existed = [pair.dst for pair in itertools.filterfalse(lambda p:
        not p.dst.exists(), paths)]

    if len(not_existed) and not force:
        raise RuntimeError(
            'The following file(s) already exists:\n'
            '{}\n'
            'Use `--force` to override.'
            .format('\n  '.join(not_existed))
          )

    for pair in paths:
        assert pair.src.is_absolute()
        assert pair.dst.is_absolute()

        try:
            dst_dir = pair.dst.parent
            if not dst_dir.exists():
                print('Creating directory: `{}`'.format(dst_dir))
                if not dry_run:
                    dst_dir.mkdir(parents=True)
            
            print('Moving `{}` to `{}`'.format(pair.src, pair.dst))
            if not dry_run:
                shutil.move(str(pair.src), str(pair.dst))

        except OSError as ex:
            raise RuntimeError(ex)


def filter_meta(pattern, metatags):
    """ Filter METADATA_FIELDS from unused tags. """
    used_tags = set()

    for metatag in metatags:
        if ('{' + metatag + '}') in pattern:
            used_tags.add(metatag)

    return used_tags
