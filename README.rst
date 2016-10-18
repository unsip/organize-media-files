What is OMF?
============
Organize Media Files (OMF) is a command-line utility, which helps user to dispatch unsorted media files according meta data tags and configurable rules. OMF using `Mutagen <https://mutagen.readthedocs.io>`_ to handle audio files. Later more media files support would be added.

Installation
============
Using \ *pip install*\ \: ::
    
    $ pip install omf

Configuration files
===================
After successful installation, user have to setup config files. OMF providing sample \ **system.conf**\  and \ **user.conf**\ . Configuration file's consist of two sections. \ *[patterns]*\  section is where user set's up dispatch path's - a \ *pattern*\ , which must be given in the form of absolute path's (\'~\' may be used to specify \ *home*\  directory) with inclusion of ``{metatags}``. 

Example audio file pattern in UNIX system\: ::

    uno = ~/Music/{artist}/{tracknumber}-{title}

Valid ``{metatags}`` for audio file are: \ ``{artist}``\ , \ ``{title}``\ , \ ``{album}``\ , \ ``{tracknumber}``\ , \ ``{genre}``\ , \ ``{date}``\ , \ ``{encoder}``\ . Due to the simplicity of utility, OMF won't lexically analyze pattern's (except for valid \ ``{metatags}``\ ), so it is up to user to specify correct pattern (use \ ``--dry-run``\  option to see what's OMF going to do).

Usage
=====
pass

TODO
============
1. Create documentation.
2. Test more formats.
3. Make a package.
4. Add bash-completion for patterns.
5. Append extensions to the end of dispathed file.

Some warnings for future
========================
1. OMF dispatching files using pathlib.Path(pattern-specified-path). Such behavior can lead to usage misunderstandings.