===============================
markov_chain
===============================


.. image:: https://img.shields.io/pypi/v/monte_carlo.svg
        :target: https://pypi.python.org/pypi/monte_carlo

.. image:: https://img.shields.io/travis/dilnoza92/monte_carlo.svg
        :target: https://travis-ci.org/dilnoza92/monte_carlo

.. image:: https://readthedocs.org/projects/monte-carlo/badge/?version=latest
        :target: https://monte-carlo.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/dilnoza92/monte_carlo/shield.svg
     :target: https://pyup.io/repos/github/dilnoza92/monte_carlo/
     :alt: Updates

.. image:: https://coveralls.io/repos/github/dilnoza92/monte_carlo/badge.svg?branch=master
:target: https://coveralls.io/github/dilnoza92/monte_carlo?branch=master

Monte Carlo simulation of Markov Chain
It is a simulation package. it takes an input as a file which should contain cordinates in tuples. input_file.txt contains an example of how it should look like.

Example input file :

(42, 46) 
(41, 32) 
(9, 41) 
(7, 28) 
(30, 40) 
(37, 14) 
(32, 10) 
(28, 34) 
(34, 3) 
(18, 43) 
(49, 12) 
(16, 1) 
(10, 50) 
(13, 36) 
(6, 33) 
(20, 8) 
(21, 30) 
(4, 40) 
(0, 49) 
(49, 25)

How to run the code with an input file
-----

* coverage run --source=monte_carlo/monte_carlo.py monte_carlo/monte_carlo.py --input_file input_file.txt

How to run the tests:
-----
*  coverage run setup.py test
*  coverage report -m



* Free software: GNU General Public License v3
* Documentation: https://monte-carlo.readthedocs.io.


Features
--------

*

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

