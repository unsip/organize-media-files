What is OMF?
============
Organize Media Files (OMF) is a command-line utility, which helps user to dispatch unsorted media files according meta data tags and configurable rules. OMF is using `Mutagen <https://mutagen.readthedocs.io>`_ to handle audio files. Later more media files support would be added.

Installation
============
Using \ *pip install*\ \: ::
    
    $ pip install organize_media_files

Getting started
===============
After successfull installation, you can see OMF doing it's job by heading into \ *example/*\ , which is located in OMF top source tree directory. ::

    $ cd example/

Here you can see `example.conf <https://github.com/IsaacMother/organize-media-files/blob/master/example/example.conf>`_ and some sample audio files, containing filled metatags. Type: ::

    $ omf -d -c example.conf sample_mp3.mp3

    Moving:
    example/sample_mp3.mp3
    To:
    /tmp/omf_example/some_artist_mp3 - some_title_mp3

You can see OMF running in \ ``--dry-run``\ . It is designed to prevent unexpected behavior and to show user what is going to happen in specified configuration. Before rushing OMF usage, don't forget to set up proper configuration using .conf files.

Configuration files
===================
OMF providing sample \ **system.conf**\  and \ **user.conf**\ , both located at \ */etc/.omfrc/*\  directory. Configuration file's consist of two sections. \ *[patterns]*\  section is where user set's up dispatch path's - a \ *pattern*\ , which must be given in the form of absolute path's (\'~\' may be used to specify \ *home*\  directory) with inclusion of ``{metatags}``. 

Example audio file pattern in UNIX system\: ::

    uno = ~/Music/{artist}/{tracknumber}-{title}

Valid ``{metatags}`` for audio file are: \ ``{artist}``\ , \ ``{title}``\ , \ ``{album}``\ , \ ``{tracknumber}``\ , \ ``{genre}``\ , \ ``{date}``\ , \ ``{encoder}``\ . Due to the simplicity of utility, OMF won't lexically analyze pattern's (except for valid \ ``{metatags}``\ ), so it is up to user to specify correct pattern (use \ ``--dry-run``\  option to see what's OMF going to do).

Usage
=====
Basic OMF usage is: ::

    $ omf filename_1 filename_2 

In this case \ ``filename_1``\  and \ ``filename_2``\  will be dispatched according to the default pattern in \ **user.conf**\ .

Options:
    * \ ``-h, --help``\  - show help message.
    * \ ``-d, --dry-run``\  - run OMF without actually moving files and print verbose information.
    * \ ``-c FILE, --config FILE``\  - specify an alternative configuration file.
    * \ ``-f, --force``\  - ignore inconsistencies or/and overwrite files (for example, if a file, in a given list of filenames, with the same name already exists, overwrite it).
    * \ ``-p PATTERN-NAME, --pattern PATTERN_NAME``\  - explicitly specify dispatch pattern.

TODO
====
1. Create documentation.
2. Figure out how to move user.conf to home directory (got bug on it).
3. Add bash-completion for patterns.
4. Append extensions to the end of dispathed file.

Some warnings for future
========================
1. OMF dispatching files using pathlib.Path(pattern-specified-path). Such behavior can lead to usage misunderstandings.