# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import types
from os.path import abspath, dirname, join
from epubcheck import utils, samples


TEST_DIR = abspath(dirname(samples.__file__))


def test_utils_java_version():
    assert utils.java_version().startswith('java version')


def test_epubcheck_help():
    assert 'listChecks' in utils.epubcheck_help()


def test_epubcheck_version():
    assert utils.epubcheck_version().startswith('EpubCheck v4.0.1')


def test_iter_files_simple():
    gen = utils.iter_files(TEST_DIR, ['py'])
    assert isinstance(gen, types.GeneratorType)
    assert len(list(gen)) == 1


def test_iter_files_no_matches():
    gen = utils.iter_files(TEST_DIR, ['noext'])
    assert len(list(gen)) == 0


def test_iter_files_flat():
    gen = utils.iter_files(TEST_DIR, ['epub'])
    assert len(list(gen)) == 2
    gen = utils.iter_files(TEST_DIR, ['EPUB'])
    assert len(list(gen)) == 2


def test_iter_files_recursive():
    gen = utils.iter_files(join('../', TEST_DIR), ['epub'], recursive=True)
    assert len(list(gen)) == 2
