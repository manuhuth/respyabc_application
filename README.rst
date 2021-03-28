Purpose
=========
This repository demonstrates how respyabc can be used in an exemplary workflow of a research project using pytask. All work is automated using the open-source software package pytask. For more information on pytask, have a look at its `documentation <https://pytask-dev.readthedocs.io/en/latest/>`_.

Directory structure
====================
The root folder contains one folder ``src``.

This folder contains the ``analysis``, ``documentation``, ``final`` and ``paper`` folders.

- ``analysis``: The analysis folder contains one file ``task_delta_history.py``. This file 	executes the short usecase of this example project, that is, two exemplary runs 			of ``respyabc.respyabc()``.
- ``documentation``: The folder ``documentation`` hosts the files with which a html style documentation can be build using `sphinx <https://www.sphinx-doc.org/en/master/>`_.
- ``final``: The folder ``final`` contains two python scripts ``task_plot_credibility_intervals.py`` and ``task_plot_kernel_density.py``. They use the data that is simulated within ``task_delta_history.py`` to create credibility intervals and kernel density estimation plots respectively. These plots are used within the document ``research_paper.tex``.
- ``paper``: This folder hosts the file ``research_paper.tex`` which consists of the Latex code for the actual paper. Furthermore, this folder contains the bibliography file ``refs.bib`` and a python script ``task_paper.py`` that automatically creates the paper PDF from ``research_paper.tex`` by running pytask.

There are no tests written in the directory of this example project since all functions are already tested within respyabc.

Installing respyabc
=====================
With ``conda`` available on your path, installing and testing
``respyabc`` is as simple as typing

.. code-block:: bash

    $ conda install -c manuhuth respyabc
    $ python -c "import respyabc; respyabc.test()"

For more information on the package check out respyabc at its `docs <https://respyabc.readthedocs.io/en/latest/>`_ or its GitHub `repository <https://github.com/manuhuth/respyabc>`_.

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://opensource.org/licenses/MIT

.. image:: https://github.com/manuhuth/respyabc/actions/workflows/ci.yml/badge.svg
   :target: https://github.com/manuhuth/respyabc/actions

.. image:: https://codecov.io/gh/manuhuth/respyabc/branch/main/graph/badge.svg?token=KvBaFo3XY3
    :target: https://codecov.io/gh/manuhuth/respyabc

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. image:: https://anaconda.org/manuhuth/respyabc/badges/version.svg
    :target: https://anaconda.org/manuhuth/respyabc


