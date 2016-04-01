# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import subprocess

JAVA_EXECUTABLE = 'java'
PROJECT_PATH = os.path.dirname(__file__)
EPUBCHECK = os.path.join(PROJECT_PATH, 'epubcheck.jar')


def java_version():
    """Call java and return version information.

    :return unicode: Java version string
    """
    result = subprocess.check_output(
        [JAVA_EXECUTABLE, '-version'], stderr=subprocess.STDOUT
    )
    first_line = result.splitlines()[0]
    return first_line.decode()


def epubcheck_version():
    """Call epubcheck and return version information.

    :return unicode: Epubcheck verstion string
    """
    with open(os.devnull, "w") as devnull:
        p = subprocess.Popen(
            [JAVA_EXECUTABLE, '-jar', EPUBCHECK, '-h'],
            stdout=subprocess.PIPE,
            stderr=devnull,
        )
        result = p.communicate()[0].splitlines()[0]
    return result.decode()
print(epubcheck_version())
