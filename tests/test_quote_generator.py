#!/usr/bin/env python

"""Tests for `quote_generator` package."""
# Third party imports
import pytest
import pandas as pd

# Package imports
from quotes.quote_engine import load_quotes, retrieve_quote
from quotes.quote import Quote


@pytest.fixture
def response():
    """
    Pytest fixture that reads in a fixed quote instance.
    """
    quotes_file = pd.read_csv('./resources/quotes/musk_quotes.csv',sep='\t')
    quote = quotes_file.iloc[12]["quote"]
    return quote

def test_loading():
    test_df = load_quotes()
    test_quote = test_df.iloc[5]
    assert test_quote["quote"] == "I keep having vivid dreams of success. Then it’s time to sleep."
    assert test_quote["author"] == "Conor Mcgregor"

def test_quote(response):
    """
    Tests the correct behaviour of the quote class.
    """
    quote_instance = Quote('Elon Musk', response)
    assert quote_instance.return_quote() == "Elon Musk: Any product that needs a manual to work is broken."

def test_quote_engine():
    """
    Tests the correct behaviour of the quote engine.
    """
    assert retrieve_quote(number=12).return_quote() == "Conor Mcgregor: I stay ready so I don’t have to get ready."