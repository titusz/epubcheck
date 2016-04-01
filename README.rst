=========================================
epubcheck - python wrappers for epubcheck
=========================================

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
    :target: https://codecov.io/github/titusz/epubcheck
    :alt: Coverage Status


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
