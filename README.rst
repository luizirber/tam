========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
        | |landscape| |scrutinizer| |codacy| |codeclimate|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/tam/badge/?style=flat
    :target: https://readthedocs.org/projects/tam
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/luizirber/tam.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/luizirber/tam

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/luizirber/tam?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/luizirber/tam

.. |requires| image:: https://requires.io/github/luizirber/tam/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/luizirber/tam/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/luizirber/tam/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/luizirber/tam

.. |landscape| image:: https://landscape.io/github/luizirber/tam/master/landscape.svg?style=flat
    :target: https://landscape.io/github/luizirber/tam/master
    :alt: Code Quality Status

.. |codacy| image:: https://img.shields.io/codacy/7c5f7a5118874cf089833ae08ef15d23.svg?style=flat
    :target: https://www.codacy.com/app/luizirber/tam
    :alt: Codacy Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/luizirber/tam/badges/gpa.svg
   :target: https://codeclimate.com/github/luizirber/tam
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/tam.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/tam

.. |downloads| image:: https://img.shields.io/pypi/dm/tam.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/tam

.. |wheel| image:: https://img.shields.io/pypi/wheel/tam.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/tam

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/tam.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/tam

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/tam.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/tam

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/luizirber/tam/master.svg?style=flat
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/luizirber/tam/


.. end-badges

Tile Assembly Model modules

* Free software: BSD license

Installation
============

::

    pip install tam

Documentation
=============

https://tam.readthedocs.org/

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
