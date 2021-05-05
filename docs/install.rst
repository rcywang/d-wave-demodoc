Installing Ocean Tools
======================


The Ocean software is a suite of tools D-Wave Systems provides on the D-Wave GitHub repository for solving hard problems with quantum computers. This section explains how to install Ocean software.

.. https://docs.ocean.dwavesys.com/en/stable/getting_started.html

* `Sign up <https://cloud.dwavesys.com/leap/login/?next=/leap/>`_ for Leap


* :ref:`Install Ocean Software <installoceansoftware>`
* :ref:`Configuring Access to D-Wave Solvers <config>`



Requirements
------------

Ocean software is supported on the following operating systems:

* Linux
* Windows (tested on 64-bit Windows 8, 10)
* Mac (tested on mac OS X 10.13)

A :ref:`Python environment <venv>` is required. Supported versions include:

* `Python 3.5 <https://www.python.org/downloads/release/python-350/>`_ and higher

.. attention:: 

    Python 2 support stopped at the end of 2019. For more information, see the `Python 3 statement <https://python3statement.org/>`_.


.. _venv:

Python Virtual Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^

It is recommended that you work in a `virtual enviornment <https://virtualenv.pypa.io/en/stable/>`_ (``venv``)

1. `Download Python <https://www.python.org/downloads/>`_ (≥ version 3.5) onto your local machine.

 For Unix-based systems, Python may be pre-installed. Installation in the command line might be as simple as:

 .. code-block:: bash

    sudo apt-get install python<version>

.. warning::

   For Windows systems, only **64-bit** Python is supported.

   

2. Install the virtualenv tool for creating isolated Python environments.

 For Unix-based systems, installation is typically done with a command such as:

 .. code-block:: bash

    sudo pip install virtualenv


3. Create a virtual environment for Ocean, such as:

   .. code-block:: bash
       
       virtualenv ocean
       source ocean/bin/activate



.. tip::

    | For `Anaconda <https://www.anaconda.com/>`_ users, activation looks like ``conda activate your_venv``,where ``your_env`` is the name of your virtual environment (in this case, ``ocean``).
    | On Windows, you might use the ``Scripts\activate`` command instead.

Your machine is now ready to install Ocean software. Learn how to :ref:`venvsetup`.


.. _installoceansoftware:

Install Ocean Software
----------------------

Via Download
^^^^^^^^^^^^

The simplest way to start is to download the `dwave-ocean-sdk <https://github.com/dwavesystems/dwave-ocean-sdk>`_ installer for the full suite of Ocean Tools.

* You can ``pip install`` the SDK inside your virtual environment. The command (compatible with Python 3.5+) looks like:

  .. code-block::
      
      pip install dwave-ocean-sdk



Via GitHub
^^^^^^^^^^

* You can also install from the source by cloning the `dwave-ocean-sdk <https://github.com/dwavesystems/dwave-ocean-sdk>`_ repository to your virtual environment. For example:

  .. code-block::
      
      git clone https://github.com/dwavesystems/dwave-ocean-sdk.git
      cd dwave-ocean-sdk
      python setup.py install



Install a Particular Tool
^^^^^^^^^^^^^^^^^^^^^^^^^

If you only wish to install a particular tool within the SDK, follow the installation instructions on the README file. For example, to download only the ``dwave-neal`` tool, navigate to the corresponding `README.rst <https://github.com/dwavesystems/dwave-neal/blob/master/README.rst>`_ file on GitHub.

For other tools, follow the links in the navigation sidebar, listed under the "TOOLS" column, for the particular tool.


.. _venvsetup:

Set Up Your Environment 
^^^^^^^^^^^^^^^^^^^^^^^

In the :ref:`virtual environment <venv>` you created, run the ``dwave setup`` command. Answer the interactive prompts to complete the setup. As an example, the output with placeholder replies is shown below:


.. include:: /docs_cli.rst
  :start-after: cli-example-setup-start-marker
  :end-before: cli-example-setup-end-marker


If you want to add packages at a later time, you can use the ``dwave install`` command:

.. code-block:: bash

    $ dwave install --help
    Usage: dwave install [OPTIONS] [PACKAGES]...

       Install optional non-open-source Ocean packages.

    Options:
      -l, --list     List available contrib (non-OSS) packages
      -a, --all      Install all contrib (non-OSS) packages
      -v, --verbose  Increase output verbosity
      --help         Show this message and exit.

Both the interactive ``dwave setup`` and ``dwave install`` commands describe the tools and enable you to select which if any to install.


Most Ocean tools may require that you configure a default `solver <https://docs.ocean.dwavesys.com/en/stable/concepts/index.html#term-Solver>`_. For the next steps in setting up your environment for D-Wave solvers, see the :ref:`Configuring Access to D-Wave Solvers <config>` page.


.. Documentation
.. -------------

.. * Access the `Ocean documentation <https://docs.ocean.dwavesys.com/en/stable/>`_
.. * Access our `Technical Support <contribute>`_


License
^^^^^^^

A list of open-source licenses may follow here:

* link to license 1
* link to license 2
* license 3
* etc.


A list of non-open-source packages that require end-user license agreements, which are provided here:

* link to EULA 1
* link to EULA 2
* EULA 3
* etc.





.. .. include:: /config.rst
..     :start-after: .. include_after_this




