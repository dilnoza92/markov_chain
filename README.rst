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

How to run the code with an input file
-----

* coverage run --source=monte_carlo/monte_carlo.py monte_carlo/monte_carlo.py --input_file input_file.txt

How to run the tests:
-----
*  coverage run setup.py test
*  coverage report -m

Before proposed distribution
----
The image before changing the adjacency matrix is named path.png
.. image:: https://github.com/dilnoza92/monte_carlo/blob/master/path.png



The Outputs
-----
The output proposed graph will  be named propsed_graph.png and saved in main directory where the setup file is saved.

.. image:: https://github.com/dilnoza92/monte_carlo/blob/master/propsed_path.png
  
The Coverage 
-------
Important! I could not make the travis work, it did not recognize my tests, hence I took a screenshot of my results from local computer 

.. image:: https://github.com/dilnoza92/monte_carlo/blob/master/screen_shot.png 




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

