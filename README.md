What is This
============

The main purpose of this software is to help to the user to dispatch unsorted
media files according meta data tags and configurable rules.


TODO
============
1. Create documentation.
2. Test more formats.
3. Make output more readable.

Some warnings for future
============
1. OMF dispatching files using pathlib.Path(pattern-specified-path). Such behavior can lead to usage misunderstandings.
2. It's up to user to write pattern correctly. Wry pattern is a user fault, not omf's. But in case omf extracting wrong metafields - have to fix `METADATA_FIELDS` list in core_varaibles.py.