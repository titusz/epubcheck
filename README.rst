=============================
Python wrappers for EpubCheck
=============================

.. image:: https://readthedocs.org/projects/epubcheck/badge/?style=flat-square
    :target: https://readthedocs.org/projects/epubcheck
    :alt: Documentation Status

.. image:: http://img.shields.io/travis/titusz/epubcheck/master.svg?style=flat-square&label=Travis
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/titusz/epubcheck

.. image:: https://img.shields.io/appveyor/ci/titusz/epubcheck/master.svg?style=flat-square&label=AppVeyor
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/titusz/epubcheck

.. image:: https://codecov.io/github/titusz/epubcheck/coverage.svg?branch=master
    :target: https://codecov.io/github/titusz/epubcheck
    :alt: Coverage Status

============
Introduction
============

The original `EpubCheck <https://github.com/w3c/epubcheck>`_ is the standard
Java based validation tool for EPUB maintained by
`DAISY Consortium <http://www.daisy.org/>`_ on behalf of the
`W3C <https://www.w3.org/publishing/epubcheck_fundraising>`_, originally
developed by the `IDPF <http://idpf.org/>`_.

This package provides a Python libary and command line tool for convenient
validation of  EPUB files by wrapping the original
`EpubCheck 4.2.2 <https://github.com/w3c/epubcheck/releases/tag/v4.2.2>`_.

* Free software: BSD license

============
Installation
============

If you have Python on your system you can do the usual::

    pip install epubcheck

You must have Python & Java installed on your system. The original Java
EpubCheck command line client itself is bundled in the
`PyPi <https://pypi.org/project/epubcheck/>`_ package.

This package is tested with Python 2.7, 3.4, 3.5, 3.6, 3.7 on Linux and Windows.
It should also work with PyPy.

==========
Quickstart
==========

Command line usage examples
---------------------------

Validata all epub files in the current directory::

    $ epubcheck

Validate a single EPUB file::

    $ epubcheck /path/to/book.epub

Validate all files in /epubfolder and create a detailed Excel report::

    $ epubcheck /path/epubfolder --xls report.xls

Show command line help::

    $ epubcheck -h


Using epubcheck as a python library
-----------------------------------

.. code-block:: pycon

    >>> from epubcheck import EpubCheck
    >>> result = EpubCheck('src/epubcheck/samples/invalid.epub')
    >>> print(result.valid)
    >>> print(result.messages)


=============
Documentation
=============

https://epubcheck.readthedocs.org/


===========
Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

=======
Credits
=======

EpubCheck is a project coordinated by `IDPF <http://idpf.org/>`_. Most of the
EpubCheck functionality comes from the schema validation tool
`Jing <https://relaxng.org/jclark/jing.html>`_  and schemas that
were developed by `IDPF <http://idpf.org/>`_ and
`DAISY <http://www.daisy.org/>`_. Initial EpubCheck development was largely
done at `Adobe Systems <https://www.adobe.com/>`_.
