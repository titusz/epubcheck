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

`EpubCheck <https://github.com/IDPF/epubcheck>`_ is the standard EPUB file
validation tool. This package provides a convenient wrapper for python.



==========
Quickstart
==========

Installation
------------

You must have Python & Java installed on your system.

EpubCheck itself is bundled on `PyPi <https://pypi.python.org/pypi/epubcheck>`_
so you only have to do the usual::

    pip install epubcheck


Usage Examples
--------------

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
