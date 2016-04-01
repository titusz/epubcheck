# -*- coding: utf-8 -*-
import epubcheck
from epubcheck import samples
from epubcheck.cli import main


def test_main():
    assert main([]) == 0


def test_valid():
    assert epubcheck.validate(samples.EPUB3_VALID)


def test_invalid():
    assert not epubcheck.validate(samples.EPUB3_INVALID)
