# -*- coding: utf-8 -*-
import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY3:
    string_types = str,
    integer_types = int,
    text_type = str
    binary_type = bytes

    MAXSIZE = sys.maxsize
else:
    string_types = basestring,
    integer_types = (int, long)
    text_type = unicode
    binary_type = str

has_scandir = True


try:
    from scandir import scandir, walk
except ImportError:
    from os import walk
    from os import listdir as scandir
    from os.path import isdir
    has_scandir = False
