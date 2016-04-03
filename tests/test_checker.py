# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from epubcheck import EpubCheck
from epubcheck import samples


def test_epubcheck_valid():
    check = EpubCheck(samples.EPUB3_VALID)
    assert check.valid is True
    assert check.checker.nError == 0


def test_epubcheck_invalid():
    check = EpubCheck(samples.EPUB3_INVALID)
    assert check.valid is False
    assert check.checker.nError == 2
