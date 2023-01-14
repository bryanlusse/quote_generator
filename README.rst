<div align="center">
<img src="quote_gen/resources/assets/logo.jpeg" alt="drawing" width="400"/> <br />


# Qoute Generator

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

![Badge](https://img.shields.io/pypi/v/quote_generator.svg)
![Badge](https://img.shields.io/travis/bryanlusse/quote_generator.svg)
![Badge](https://readthedocs.org/projects/quote-generator/badge/?version=latest)
![Badge](https://img.shields.io/github/languages/code-size/bryanlusse/quote_generator)
![Badge](https://img.shields.io/github/languages/count/bryanlusse/quote_generator)
![Badge](https://img.shields.io/github/last-commit/bryanlusse/quote_generator)

[Overview](#scroll-overview)
•
[How to use](#chart_with_upwards_trend-model)
•
[Installation](#floppy_disk)
</div>

## :bookmark_tabs: Menu

- [Overview](#scroll-overview)
- [Documentation](#books)
- [How to use](#chart_with_upwards_trend-model)
- [Installation](#floppy_disk)
- [Requirements](#exclamation-requirements)
- [Folder Structure](#closedbook-results)
- [Author](#smiley_cat-author)
- [Credits](#copyright)

## :scroll: Overview

This project contains code for an API interface that generates random quotes. 
I created this project in order to improve and display my skills in data and code engineering.

Future developments:
- [ ] Adding to PyPI
- [ ] Using Docker
- [ ] Actual deployment on Heroku
- [ ] Using a different datasource.

## :books: Documentation

The docs can be found on https://quote-generator.readthedocs.io.

## :closed_book: How to use

:construction::construction::construction: This will be updated once the application is running on a server. :construction::construction::construction:

## :floppy_disk: Installation

Clone the code using:

.. code-block:: shell
        $ git@github.com:bryanlusse/quote_generator.git

Then create a virtual environment and install all requirements using:

.. code-block:: shell
        $ virtualenv -p python3.11.1 venv 
        $ source venv/bin/activate 
        $ pip install -r requirements_dev.txt

You can then run your own version of the *quote_generator* locally by running:

.. code-block:: shell
        $ uvicorn quote_gen.api.main:app --reload --port 8000

You can then access the API interface on http://127.0.0.1:8000.
Access the API docs on http://127.0.0.1:8000/docs

## :exclamation: Requirements

Found in [requirements_dev.txt](https://github.com/bryanlusse/quote_generator/blob/master/requirements_dev.txt).

## :open_file_folder: Folder Structure

.. code_block::
        .
        ├── docs                                # The documentation lives here
        ├── quote_gen                           # The main code lives here
        ├── requirements_dev.txt                # Required packages
        ├── Makefile
        └── README.rst

All files can be inspecte on Github.

## :smiley_cat: Author

- [@bryanlusse](https://github.com/bryanlusse)

Made with &nbsp;❤️&nbsp;

## :copyright: Credits

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
