What is This
============

The main purpose of this software is to help to the user to dispatch unsorted
media files according meta data tags and configurable rules.


TODO
============
1. Check if everything is ok.
2. Test more formats.
3. Add more metatag fields.
4. Complete exception raises (exception texts).

Some warnings for future
============
1. OMF dispatching files using pathlib.Path(pattern-specified-path). Such behavior can lead to usage misunderstandings. (Can pathlib constuct paths, using OS vars?)