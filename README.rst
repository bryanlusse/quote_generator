.. image:: quote_gen/resources/assets/logo.jpeg

Qoute Generator
==================

.. container::

.. rubric::

|Python| |FastAPI|

|Badge1| |Badge2| |Badge3| |Badge4| |Badge5| |Badge6|

Menu
--------------------

-  `Overview`
-  `Documentation` 
-  `How to use`
-  `Installation`
-  `Requirements`
-  `Folder Structure`
-  `Author`
-  `Credits`

Overview
-----------------

This project contains code for an API interface that generates random
quotes. I created this project in order to improve and display my skills
in data and code engineering.

Future developments: 
- Adding to PyPI 
- Using Docker 
- Actual deployment on Heroku 
- Using a different datasource.

Documentation
---------------------

The docs can be found on https://quote-generator.readthedocs.io.

How to use
------------------------

:construction::construction::construction: This will be updated once the
application is running on a server.
:construction::construction::construction:

Installation
--------------------------

Clone the code using:

.. raw:: html

   <pre><code>
   $ git@github.com:bryanlusse/quote_generator.git
   </code></pre>

Then create a virtual environment and install all requirements using:

.. raw:: html

   <pre><code>
   $ virtualenv -p python3.11.1 venv 
   $ source venv/bin/activate 
   $ pip install -r requirements_dev.txt
   </code></pre>

You can then run your own version of the *quote_generator* locally by
running:

.. raw:: html

   <pre><code>
   $ uvicorn quote_gen.api.main:app --reload --port 8000
   </code></pre>

You can then access the API interface on http://127.0.0.1:8000. Access
the API docs on http://127.0.0.1:8000/docs

Requirements
--------------------------

Found in
`requirements_dev.txt <https://github.com/bryanlusse/quote_generator/blob/master/requirements_dev.txt>`__.

Folder Structure
-----------------------------------

.. raw:: html

   <pre><code>
   .
   ├── docs                                # The documentation lives here
   ├── quote_gen                           # The main code lives here
   ├── requirements_dev.txt                # Required packages
   ├── Makefile
   └── README.rst
   </code></pre>

All files can be inspected on Github.

Author
-------------------

-  `@bryanlusse <https://github.com/bryanlusse>`__

Made with love.

Credits
-------------------

This package was created with
`Cookiecutter <https://github.com/audreyr/cookiecutter>`__ and the
`audreyr/cookiecutter-pypackage <https://github.com/audreyr/cookiecutter-pypackage>`__
project template.

.. |Python| image:: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
.. |FastAPI| image:: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
.. |Badge1| image:: https://img.shields.io/pypi/v/quote_generator.svg
.. |Badge2| image:: https://img.shields.io/travis/bryanlusse/quote_generator.svg
.. |Badge3| image:: https://readthedocs.org/projects/quote-generator/badge/?version=latest
.. |Badge4| image:: https://img.shields.io/github/languages/code-size/bryanlusse/quote_generator
.. |Badge5| image:: https://img.shields.io/github/languages/count/bryanlusse/quote_generator
.. |Badge6| image:: https://img.shields.io/github/last-commit/bryanlusse/quote_generator
