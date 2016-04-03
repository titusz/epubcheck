# -*- coding: utf-8 -*-
from os import path

ROOT = path.abspath(path.dirname(__file__))

EPUB3_VALID = path.join(ROOT, 'childrens-literature.epub')
EPUB3_INVALID = path.join(ROOT, 'invalid.epub')
RESULT_VALID = path.join(ROOT, 'result_valid.json')
RESULT_INVALID = path.join(ROOT, 'result_invalid.json')
