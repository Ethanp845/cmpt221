.. _`Development`:

Development
===========
This section is intended for developers that want to create a fix or develop an enhancement to the CMPT221 Lab Repository.

Code of Conduct
---------------
- Follow standard Python coding conventions (PEP 8)
- Write meaningful commit messages
- Include docstrings for all functions and classes
- Test code thoroughly before submitting

Repository
----------
The repository for CMPT221 Lab Repository is on Github: 

Development Environment
-----------------------
A `Python virtual environment`_ is recommended. Once the virtual environment is activated, clone the CMPT221 repository and prepare the development environment with:

.. _Python virtual environment: https://virtualenv.pypa.io/en/latest/

.. code-block:: text

    $ git clone https://github.com/Ethanp845/cmpt221.git
    $ cd cmpt221
    $ pip install -r requirements.txt

This will install all local prerequisites needed for the CMPT221 labs to run.

Pytest
------
Unit tests are developed using Pytest. To run the test suite, issue:

.. code-block:: text

    $ cd tests
    $ pytest <filename.py>

Build Documentation
-------------------
The Github pages site is used to publish documentation for the CMPT221 Lab Repository.

To build the documentation, issue:

.. code-block:: text
    
    $ cd docs
    $ make html
    # windows users without make installed use:
    $ make.bat html

The top-level document to open with a web-browser will be ``docs/_build/html/index.html``.

To publish the page, copy the contents of the directory ``docs/_build/html`` into the branch
``gh-pages``. Then, commit and push to ``gh-pages``.