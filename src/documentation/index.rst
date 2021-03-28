.. This the respyabc application project's documentation master file.

.. You can adapt this file completely to your liking,
.. but it should at least contain the `toctree` directive.


Welcome to the documentation of the respyabc example project!
================================================================================================
This project demonstrates how `respyabc <https://respyabc.readthedocs.io/en/latest/>`_ can be used in an exemplary workflow of a research project. For the template see `here <https://respyabc.readthedocs.io/en/latest/>`_. Within the example project, one exemplary data set is simulated and evaluated using the routines implemented in respyabc.
All work is automated using the open-source software package pytask. For more information on pytask, have a look at its `documentation <https://pytask-dev.readthedocs.io/en/latest/>`_.

For more information on the package check out respyabc at its `online documentation <https://respyabc.readthedocs.io/en/latest/>`_ or its GitHub `repository <https://github.com/manuhuth/respyabc>`_.

Getting started
================
In order to run this project on your local machine you need to clone it from the `repository <https://github.com/manuhuth/respyabc_application>`_, have Python installed and a modern LaTex distribution in order to compile .tex documents. After cloning the repository, it is highly recommended to create a new virtual environemnt from the environment.yml file in order to ensure that all package dependencies are installed.

.. code-block:: bash

    $ conda env create -f environment.yml
    $ conda activate respyabc

To run the project with pytask a user needs to create a ``conda.pth`` file in site-packages on her local machine. The easiest way doing so is to navigate to the root directory (the path to which the repository has been cloned) and type

.. code-block:: bash

    $ conda develop .

Being inside the root directory one can simply run the project with pytask by typing

.. code-block:: bash

    $ pytask

The project is created, run and tested on Linux-Pop!_OS 20.04 but is supposed to work on Windows and MacOS as well.

.. toctree::
    :maxdepth: 2

    introduction
    analysis
    final
    paper
    references
