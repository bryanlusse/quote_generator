#!/usr/bin/env python

"""Tests for `quote_generator` package."""
# Native imports
import os
import importlib.resources
# Third party imports
import pytest
import pandas as pd
# Package imports
from quotes.quote_engine import load_quotes, retrieve_quote
from quotes.quote import Quote


@pytest.fixture(name="response_quote")
def fixture_response_quote():
    """
    Pytest fixture that reads in a fixed quote instance.
    """
    resources_path = str(importlib.resources.files('resources.quotes'))
    quotes_file = pd.read_csv(os.path.join(resources_path,'musk_quotes.csv'),sep='\t')
    quote = quotes_file.iloc[12]["quote"]
    return quote

def test_loading():
    """
    Tests loading of all quotes.
    """
    test_df = load_quotes()
    example_quote = test_df.iloc[5]
    assert example_quote["quote"] == "I keep having vivid dreams of success. Then it’s time" \
        " to sleep."
    assert example_quote["author"] == "Conor Mcgregor"

def test_quote(response_quote):
    """
    Tests the correct behaviour of the quote class.
    """
    quote_instance = Quote('Elon Musk', response_quote)
    assert quote_instance.return_quote() == "Elon Musk: Any product that needs a manual" \
        " to work is broken."

def test_quote_engine():
    """
    Tests the correct behaviour of the quote engine.
    """
    assert retrieve_quote(number=12).return_quote() == "Conor Mcgregor: I stay ready so" \
        " I don’t have to get ready."
