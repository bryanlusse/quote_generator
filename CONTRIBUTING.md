# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at [quote_generator Issues](https://github.com/bryanlusse/quote_generator/issues).

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement" and "help wanted" is open to whoever wants to implement it.

### Write Documentation

Quote Generator could always use more documentation, whether as part of the official Quote Generator docs, in docstrings, or even on the web in blog posts, articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at [quote_generator Issues](https://github.com/bryanlusse/quote_generator/issues).

If you are proposing a feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions are welcome :)

## Get Started!

Ready to contribute? Here's how to set up `quote_generator` for local development.

1. Fork the `quote_generator` repo on GitHub.
2. Clone your fork locally:

   ```shell
   $ git clone git@github.com:your_name_here/quote_generator.git
   ```

3. Then create a virtual environment and install all requirements using:

    ```shell
    $ pip install poetry
    $ poetry lock
    $ source .venv/bin/activate
    $ poetry install
    ```

4. Create a branch for local development:

    ```shell
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

5. Make your changes
6. Commit your changes and push your branch to GitHub:

    ```shell
    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature
    ```

7. Submit a pull request through the GitHub website.

## Pull Request Guidelines
Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put your new functionality into a function with a docstring, and add the feature to the list in README.md.
3. The pull request should work for Python 3.5, 3.6, 3.7, and 3.8, and for PyPy. Check Travis CI Pull Requests and make sure that the tests pass for all supported Python versions.