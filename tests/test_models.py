# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from epubcheck import compat, models, samples


VALID = json.load(open(samples.RESULT_VALID))
INVALID = json.load(open(samples.RESULT_INVALID))


def test_checker_from_data():
    checker = models.Checker.from_data(VALID)
    assert isinstance(checker, models.Checker)


def test_meta_from_data():
    meta = models.Meta.from_data(VALID)
    assert isinstance(meta, models.Meta)
    assert isinstance(meta.title, compat.text_type)
    assert isinstance(meta.creator, list)
    assert isinstance(meta.isScripted, bool)
    assert isinstance(meta.charsCount, int)


def test_message_from_data_valid_returns_list():
    msgs = models.Message.from_data(VALID)
    assert isinstance(msgs, list)
    assert len(msgs) == 0


def test_message_from_data_invalid_returns_list():
    msgs = models.Message.from_data(INVALID)
    assert isinstance(msgs, list)
    assert isinstance(msgs[0], models.Message)
    assert len(msgs) == 4
