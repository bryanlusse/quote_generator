#!/usr/bin/env python

"""Tests for `interface` module."""
# Package imports
from quote_gen.api.main import root, get_quote

def test_root():
    """
    Tests the working of the API root.
    """
    assert root() == {"message": "Hello and welcome to the quote API"}

def test_quote():
    """
    Tests the retrieval of the quote for the API function.
    """
    result = get_quote()
    assert result['message']
