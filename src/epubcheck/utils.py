# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import subprocess

from epubcheck import samples
from epubcheck import const as c
from epubcheck.checker import EpubCheck


def java_version():
    """Call java and return version information.

    :return unicode: Java version string
    """
    result = subprocess.check_output(
        [c.JAVA, '-version'], stderr=subprocess.STDOUT
    )
    first_line = result.splitlines()[0]
    return first_line.decode()


def epubcheck_help():
    """Return epubcheck.jar commandline help text.

    :return unicode: helptext from epubcheck.jar
    """

    # tc = locale.getdefaultlocale()[1]

    with open(os.devnull, "w") as devnull:
        p = subprocess.Popen(
            [c.JAVA, '-Duser.language=en', '-jar', c.EPUBCHECK, '-h'],
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


def generate_sample_json():
    """Generate sample json data for testing"""

    check = EpubCheck(samples.EPUB3_VALID)
    with open(samples.RESULT_VALID, 'wb') as jsonfile:
        jsonfile.write(check._stdout)

    check = EpubCheck(samples.EPUB3_INVALID)
    with open(samples.RESULT_INVALID, 'wb') as jsonfile:
        jsonfile.write(check._stdout)

if __name__ == "__main__":
    generate_sample_json()
