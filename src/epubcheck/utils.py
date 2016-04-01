# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import subprocess
import locale
from epubcheck import const as c


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

    tc = locale.getdefaultlocale()[1]

    with open(os.devnull, "w") as devnull:
        p = subprocess.Popen(
            [c.JAVA, '-jar', c.EPUBCHECK, '-h'],
            stdout=subprocess.PIPE,
            stderr=devnull,
        )
        result = p.communicate()[0]

    return result.decode(tc)


def epubcheck_version():
    """Call epubcheck -h and return helptext.

    :return unicode: Epubcheck verstion string
    """
    return epubcheck_help().splitlines()[0]


if __name__ == "__main__":
    print(epubcheck_help())
