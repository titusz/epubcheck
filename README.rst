=============================
Python wrappers for EpubCheck
=============================

.. image:: https://readthedocs.org/projects/epubcheck/badge/?style=flat
    :target: https://readthedocs.org/projects/epubcheck
    :alt: Documentation Status

.. image:: https://travis-ci.org/titusz/epubcheck.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/titusz/epubcheck

.. image:: https://ci.appveyor.com/api/projects/status/github/titusz/epubcheck?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/titusz/epubcheck

.. image:: https://codecov.io/github/titusz/epubcheck/coverage.svg?branch=master
    :target: https://codecov.io/github/titusz/epubcheck
    :alt: Coverage Status

============
Introduction
============

The original `EpubCheck <https://github.com/IDPF/epubcheck>`_ is the standard
Java based validation tool for |EPUB| provided by the
`|IDPF| <http://http://idpf.org/>`_

This package provides a Python libary and command line tool for convenient
validation of  |EPUB| files by wrapping the original
`EpubCheck <https://github.com/IDPF/epubcheck>`_.

* Free software: BSD license

============
Installation
============

If you have Python on your system you can do the usual::

    pip install epubcheck

You must have Python & Java installed on your system. The original Java
EpubCheck command line client itself is bundled in the
`PyPi <https://pypi.python.org/pypi/epubcheck>`_ package.

This package is tested with Python 2.7, 3.3, 3.4, 3.5 on Linux and Windows.
It should also work with PyPy.

----------
Quickstart
----------

Command line usage examples
---------------------------

Validate a single |EPUB| file from the command line::

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


Documentation
=============

https://epubcheck.readthedocs.org/

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


Credits
=======

EpubCheck is a project coordinated by `IDPF <http://idpf.org/>`_. Most of the
EpubCheck functionality comes from the schema validation tool
`Jing <http://www.thaiopensource.com/relaxng/jing.html>`_  and schemas that
were developed by `IDPF <http://idpf.org/>`_ and
`DAISY <http://www.daisy.org/>`_. Initial EpubCheck development was largely
done at `Adobe Systems <http://www.adobe.com/>`_.


.. |IDPF| raw:: html
    <abbr title="International Digital Publishing Forum">IDPF</abbr>

.. |EPUB| raw:: html
    <abbr title="electronic publication">EPUB</abbr>

