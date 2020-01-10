# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys

import pytest
import tablib

import epubcheck
from epubcheck import samples
from epubcheck.cli import main


def test_valid():
    assert epubcheck.validate(samples.EPUB3_VALID)


def test_invalid():
    assert not epubcheck.validate(samples.EPUB3_INVALID)


def test_main_valid(capsys):
    argv = [samples.EPUB3_VALID]
    exit_code = main(argv)
    out, err = capsys.readouterr()
    assert 'ERROR' not in out and 'ERROR' not in err
    assert exit_code == 0


def test_main_invalid(capsys):
    argv = [samples.EPUB3_INVALID]
    exit_code = main(argv)
    out, err = capsys.readouterr()
    assert 'ERROR' in err and 'WARNING' in out
    assert exit_code == 1


def test_csv_report(tmp_path):
    results_file = tmp_path / 'results.csv'
    main([samples.EPUB3_INVALID, '--csv', str(results_file)])

    with results_file.open('r') as f:
        dataset = tablib.Dataset().load(f.read(), format='csv', delimiter=';')
        assert dataset[0][:3] == ('OPF-003', 'WARNING', 'invalid.epub')


def test_xls_report(tmp_path):
    results_file = tmp_path / 'results.xls'
    main([samples.EPUB3_INVALID, '--xls', str(results_file)])

    with results_file.open('rb') as f:
        databook = tablib.Databook().load(f.read(), format='xls')
        assert databook.sheets()[1][0][:3] == ('OPF-003', 'WARNING', 'invalid.epub')
