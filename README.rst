========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor|
        | |codecov|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/epubcheck/badge/?style=flat
    :target: https://readthedocs.org/projects/epubcheck
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/titusz/epubcheck.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/titusz/epubcheck

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/titusz/epubcheck?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/titusz/epubcheck

.. |codecov| image:: https://codecov.io/github/titusz/epubcheck/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/titusz/epubcheck

.. |version| image:: https://img.shields.io/pypi/v/epubcheck.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/epubcheck

.. |downloads| image:: https://img.shields.io/pypi/dm/epubcheck.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/epubcheck

.. |wheel| image:: https://img.shields.io/pypi/wheel/epubcheck.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/epubcheck

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/epubcheck.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/epubcheck

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/epubcheck.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/epubcheck


.. end-badges

Python epubcheck wrapper

* Free software: BSD license

Installation
============

::

    pip install epubcheck

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
