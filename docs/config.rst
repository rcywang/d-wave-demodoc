.. _config:

Configuration
-------------

This section uses the `Initial Set Up <https://docs.ocean.dwavesys.com/en/stable/getting_started.html#initial-set-up>`_ instructions from D-Wave's official `Ocean Documentation <https://docs.ocean.dwavesys.com/en/stable/index.html>`_ and is meant as a placeholder and example for the configuration section of software installation/documentation.

----

Creating a Configuration File 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The simplest way to configure solver access is to use the `interactive CLI <https://docs.ocean.dwavesys.com/en/stable/docs_cli.html#dwave-cli>`_, which is installed as part of the `dwave-ocean-sdk <https://github.com/dwavesystems/dwave-ocean-sdk>`_ installation.

If you have not already done so with the ``dwave setup`` command in the :ref:`Set Up Your Environment <venvsetup>` section, or want to make changes at a later time, you can use the ``dwave config`` command:

.. code-block:: bash

    $ dwave config --help
    Usage: dwave config [OPTIONS] COMMAND [ARGS]...

    Create, update or inspect cloud client configuration file(s).

    Options:
      --help  Show this message and exit.

    Commands:
      create   Create and/or update cloud client configuration file.
      inspect  Inspect existing configuration/profile.
      ls       List configuration files detected (and/or examined paths).


A step-by-step tutorial on creating a configuration file using the ``dwave config create`` command can be found `here <https://docs.ocean.dwavesys.com/en/stable/overview/sapi.html#creating-a-configuration-file>`_. 

Alternatively, you can create and edit a `D-Wave Cloud Client Configuration file <https://docs.ocean.dwavesys.com/en/stable/docs_cloud/sdk_index.html>`_ manually.



Verifying Your Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can test that your solver access is configured correctly with the  `interactive CLI <https://docs.ocean.dwavesys.com/en/stable/docs_cli.html#dwave-cli>`_, using the ``dwave ping`` or ``dwave sample --random-problem`` commands.

See `D-Wave's Verifying Your Configuration <https://docs.ocean.dwavesys.com/en/stable/overview/sapi.html#verifying-your-configuration>`_ page.


Querying Available Solvers
^^^^^^^^^^^^^^^^^^^^^^^^^^

From the terminal, you can use the `interactive CLI <https://docs.ocean.dwavesys.com/en/stable/docs_cli.html#dwave-cli>`_ to see the available solvers, their parameters, and properties. 

See `D-Wave's Querying Available Solvers <https://docs.ocean.dwavesys.com/en/stable/overview/sapi.html#querying-available-solvers>`_ page.

.. tip:: 

    `Leap <https://cloud.dwavesys.com/leap/>`_ accounts can see accessible solvers on the dashboard.
