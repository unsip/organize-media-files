# Standard imports
import argparse
import click
import exitstatus
import os
import pathlib
import sys

# Project-specific imports
from .config import config as config_holder
from .extractor import extractor
from .organaizer import dispatch, apply_move 

SYSTEM_CONFIG = '/etc/omf.conf'
USER_CONF = '.omfrc'

@click.command()
@click.option(
    '--dry-run',
    '-d',
    is_flag=True,
    default=False,
    help='Do not do the job, just show whats going to be done'
)
@click.option(
    '--config',
    '-c',
    metavar='FILENAME',
    default=None,
    help='Specify an alternative configuration file',
)
@click.option(
    '--force',
    '-f',
    is_flag=True,
    default=False,
    help='Ignore inconsistencies or/and overwrite files'
)
@click.option(
    '--pattern',
    '-p',
    metavar='PATTERN-STRING',
    help='Use given pattern to dispatch incoming files'
)
@click.argument(
    'input-file',
    nargs=-1,
)
def cli(dry_run, config, force, pattern, input_file):
    if config is not None:
        cfg_file = pathlib.Path(config)
        _config = config_holder(cfg_file)
    else:
        # Check if system-wide config is here
        system_cfg_file = pathlib.Path(SYSTEM_CONFIG)
        system_conf = None
        if system_cfg_file.exists():
            system_conf = config_holder(system_cfg_file)

        # Check user config
        user_cfg_file = pathlib.Path(pathlib.Path.home() / USER_CONF)

        user_conf = None
        if user_cfg_file.exists():
            user_conf = config_holder(user_cfg_file)

        if system_conf and user_conf:
            _config = user_conf
            _config.merge_from(system_conf)
        elif system_conf:
            _config = system_conf
        elif user_conf:
            _config = user_conf
        else:
            emsg = 'No config file has been found/given. ' \
                'Create `.omfrc` in your $HOME directory.'
            raise RuntimeError(emsg)

    if pattern:
        _config.pattern = pattern

    paths = dispatch(input_file, _config.pattern, force)
    apply_move(paths, force, dry_run) 
    
    return exitstatus.ExitStatus.success

def main():
    try:
        return cli()
    except KeyboardInterrupt:
        return exitstatus.ExitStatus.failure
    except RuntimeError as ex:
        print('*** Error: {}'.format(ex))
        return exitstatus.ExitStatus.failure
