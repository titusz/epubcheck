# Python wrappers and CLI for EpubCheck

[![Linux/Windows/macOS Tests](https://github.com/titusz/epubcheck/workflows/Tests/badge.svg)](https://github.com/titusz/epubcheck/actions?query=workflow%3ATests)
[![Version](https://img.shields.io/pypi/v/epubcheck.svg)](https://pypi.python.org/pypi/epubcheck/)

> A command line tool and lib that wraps EpubCheck for Python.

## Introduction

The original [EpubCheck](https://github.com/w3c/epubcheck) is the standard
Java based validation tool for EPUB maintained by
[DAISY Consortium](https://daisy.org/) on behalf of the
[W3C](https://www.w3.org/publishing/epubcheck_fundraising), originally
developed by the [IDPF](http://idpf.org/).

This package provides a Python libary and command line tool for convenient
validation of  EPUB files by wrapping the original
[EpubCheck 4.2.6](https://github.com/w3c/epubcheck/releases/tag/v4.2.6).

* Free software: BSD license

## Installation

If you have Python on your system you can do the usual:

    $ pip install epubcheck


You must have Python & Java installed on your system. The original Java
EpubCheck command line client itself is bundled in the
[PyPi](https://pypi.org/project/epubcheck/) package.

This package is tested with Python 3.8 - 3.12 on Linux, Mac and Windows.
It should also work with PyPy.

## Quickstart


### Command line usage examples

Validata all epub files in the current directory:

    $ epubcheck

Validate a single EPUB file:

    $ epubcheck /path/to/book.epub

Validate all files in /epubfolder and create a detailed Excel report::

    $ epubcheck /path/epubfolder --xls report.xls

Show command line help::

    $ epubcheck -h


### Using epubcheck as a python library


```python
from epubcheck import EpubCheck
result = EpubCheck('src/epubcheck/samples/invalid.epub')
print(result.valid)
print(result.messages)
```

## Documentation
https://epubcheck.readthedocs.io/en/latest/

## Development

Install [poetry](https://pypi.org/project/poetry/) checkout this repository and run:

    poetry install


## Changelog

### [4.2.6] - 2021-11-06
- Bump versioning to match original epubcheck version
- Modernize packaging and CI
- Fix xls and csv export
- Updated dependencies

### [0.4.3] - 2021-09-28
- Update the epubcheck.jar to v4.2.6
- Remove support for < Python 3.6

### [0.4.2] - 2019-08-07
- Update the epubcheck.jar to v4.2.2 (see: https://github.com/w3c/epubcheck/releases/tag/v4.2.2)

### [0.3.1] - 2016-04-20
- Added custom PY2/PY3 compat module and removed dependancy on six

### [0.3.0] - 2016-04-10
- Add commandline support with Excel batch reporting
- Moved development status from Alpha to Beta

### [0.2.0] - 2016-04-03
- EpubCheck results as native python objects
- More documentation

### [0.1.0] - 2016-04-01
-  First release on PyPI.


## Authors & Contributors
- Titusz Pan - https://github.com/titusz
- Sean Quinn - https://github.com/swquinn
- Curtis Smith - https://github.com/csmithd

## Credits

EpubCheck is a project coordinated by [IDPF](http://idpf.org/). Most of the
EpubCheck functionality comes from the schema validation tool
[Jing](https://relaxng.org/jclark/jing.html) and schemas that
were developed by [IDPF](http://idpf.org/) and
[DAISY](https://daisy.org/). Initial EpubCheck development was largely
done at [Adobe Systems](https://www.adobe.com/).
