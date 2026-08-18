import json
from epubcheck import models, samples


with open(samples.RESULT_VALID) as f:
    VALID = json.load(f)

with open(samples.RESULT_INVALID) as f:
    INVALID = json.load(f)


def test_checker_from_data():
    checker = models.Checker.from_data(VALID)
    assert isinstance(checker, models.Checker)


def test_meta_from_data():
    meta = models.Meta.from_data(VALID)
    assert isinstance(meta, models.Meta)
    assert isinstance(meta.title, str)
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
    assert len(msgs) == 3
    assert str(msgs[0]).startswith("OPF-004 | WARNING")
