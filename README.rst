=========================================
epubcheck - python wrappers for epubcheck
=========================================


.. image:: http://img.shields.io/travis/titusz/epubcheck/master.svg?style=flat-square&label=Travis
    :target: https://travis-ci.org/titusz/epubcheck
    :alt: Travis-CI Build Status


.. image:: https://img.shields.io/appveyor/ci/titusz/epubcheck/master.svg?style=flat-square&label=AppVeyor
    :target: https://ci.appveyor.com/project/titusz/epubcheck
    :alt: AppVeyor Build Status


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
