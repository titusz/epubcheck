# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from epubcheck import utils


def test_utils_java_version():
    assert utils.java_version().startswith('java version')


def test_epubcheck_help():
    assert 'listChecks' in utils.epubcheck_help()


def test_epubcheck_version():
    assert utils.epubcheck_version().startswith('EpubCheck v4.0.1')
