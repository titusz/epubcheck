# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import subprocess
from epubcheck import const as c


def validate(epub_path):
    """Minimal validation.

    :return bool: True if valid else False
    """

    try:
        subprocess.check_call([c.JAVA, '-jar', c.EPUBCHECK, epub_path])
        return True
    except subprocess.CalledProcessError:
        return False
