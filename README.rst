|build| |version| |wheel|

ShadeTree OBD
=============

ShadeTree OBD provides easy access to ELM327 OBD-II Interfaces in Python.
It's been successfully used with ELM327 OBD-II bluetooth scanners and the Raspberry Pi to create portable automotive
OBD-II logging devices.  Data can be captured during test drives for later analysis.  It may also be used as part of
routine driving to gather information to determine an optimal vehicle maintenance schedule.  Continuous logging may
also help with vehicle troubleshooting when problems occur.

This library was originally developed as a teaching tool to help the best rural problem solvers get excited about
computing via their existing passion for automotive work.

The library is still under development.  Initial work focused on reading from and writing to ELM327 OBD-II interfaces.
Work is ongoing to build more tools and services around the core library.

Installation
------------

Install using pip_

.. code-block:: bash

    $ pip install shadetree

Quick start
-----------

.. code-block:: python

    from shadetree.obd.scanner import OBDScanner

    with OBDScanner() as obd:
        print('ELM version'.format(obd.elm_version))
        print('Vehicle Identification Number (VIN): {0}'.format(obd.vehicle_id_number()))
        print('Engine Control Unit (ECU) Name: {0}'.format(obd.ecu_name()))
        print('Battery voltage: {0}'.format(obd.battery_voltage()))
        print('Fuel type: {0}'.format(obd.fuel_type()))
        print('Coolant temp: {0}'.format(obd.current_engine_coolant_temperature()))
        print('Oil temp: {0}'.format(obd.current_engine_oil_temperature()))
        print('Engine RPM: {0}'.format(obd.current_engine_rpm()))

Supported Python Versions
-------------------------

ShadeTree OBD makes every effort to ensure smooth operation with these Python interpreters:

* 2.7+
* 3.4+
* PyPy

License
-------

See LICENSE_ for details.

.. _pip: https://pypi.python.org/pypi/pip
.. _LICENSE: LICENSE.txt

.. |version| image:: https://badge.fury.io/py/shadetree.svg
    :target: https://pypi.python.org/pypi/shadetree/

.. |build| image:: https://api.travis-ci.org/corbinbs/shadetree.svg
    :target: https://travis-ci.org/corbinbs/shadetree

.. |wheel| image:: https://pypip.in/wheel/shadetree/badge.png
    :target: https://pypi.python.org/pypi/shadetree/
