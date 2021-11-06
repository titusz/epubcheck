# -*- coding: utf-8 -*-
import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY3:
    string_types = (str,)
    integer_types = (int,)
    text_type = str
    binary_type = bytes

    MAXSIZE = sys.maxsize
else:
    string_types = (basestring,)  # NOQA
    integer_types = (int, long)  # NOQA
    text_type = unicode  # NOQA
    binary_type = str

has_scandir = True


try:
    from scandir import scandir, walk
except ImportError:
    from os import walk  # NOQA
    from os import listdir as scandir  # NOQA
    from os.path import isdir  # NOQA

    has_scandir = False
