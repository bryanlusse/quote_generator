#!/usr/bin/env python

"""Tests for `interface` module."""
# Package imports
from quote_gen.interface.cli import main

def test_cli():
    """
    Tests the correct working of the CLI main function.
    """
    assert main() == 0
