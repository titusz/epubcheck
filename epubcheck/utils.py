# -*- coding: utf-8 -*-
"""Generic or common utility functions"""

from __future__ import print_function, unicode_literals
import os
from os.path import splitext, join
import subprocess
from epubcheck import samples
from epubcheck import const as c
from epubcheck import compat
from epubcheck.checker import EpubCheck


def java_version():
    """Call java and return version information.

    :return unicode: Java version string
    """
    result = subprocess.check_output([c.JAVA, "-version"], stderr=subprocess.STDOUT)
    first_line = result.splitlines()[0]
    return first_line.decode()


def epubcheck_help():
    """Return epubcheck.jar commandline help text.

    :return unicode: helptext from epubcheck.jar
    """

    # tc = locale.getdefaultlocale()[1]

    with open(os.devnull, "w") as devnull:
        p = subprocess.Popen(
            [c.JAVA, "-Duser.language=en", "-jar", c.EPUBCHECK, "-h"],
            stdout=subprocess.PIPE,
            stderr=devnull,
        )
        result = p.communicate()[0]

    return result.decode()


def epubcheck_version():
    """Call epubcheck -h and return helptext.

    :return unicode: Epubcheck verstion string
    """
    return epubcheck_help().splitlines()[0]


def generate_sample_json():  # pragma: no cover
    """Generate sample json data for testing"""

    check = EpubCheck(samples.EPUB3_VALID)
    with open(samples.RESULT_VALID, "wb") as jsonfile:
        jsonfile.write(check._stdout)

    check = EpubCheck(samples.EPUB3_INVALID)
    with open(samples.RESULT_INVALID, "wb") as jsonfile:
        jsonfile.write(check._stdout)


def iter_files(root, exts=None, recursive=False):
    """
    Iterate over file paths within root filtered by specified extensions.
    :param compat.string_types root: Root folder to start collecting files
    :param iterable exts: Restrict results to given file extensions
    :param bool recursive: Wether to walk the complete directory tree
    :rtype collections.Iterable[str]: absolute file paths with given extensions
    """

    if exts is not None:
        exts = set((x.lower() for x in exts))

    def matches(e):
        return (exts is None) or (e in exts)

    if recursive is False:
        for entry in compat.scandir(root):
            if compat.has_scandir:  # pragma: no cover
                ext = splitext(entry.name)[-1].lstrip(".").lower()
                if entry.is_file() and matches(ext):
                    yield entry.path
            else:
                ext = splitext(entry)[-1].lstrip(".").lower()
                if not compat.isdir(entry) and matches(ext):
                    yield join(root, entry)
    else:
        for root, folders, files in compat.walk(root):
            for f in files:
                ext = splitext(f)[-1].lstrip(".").lower()
                if matches(ext):
                    yield join(root, f)


if __name__ == "__main__":
    generate_sample_json()  # pragma: no cover
