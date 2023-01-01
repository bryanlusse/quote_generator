#!/usr/bin/env python

"""Tests for `quote_generator` package."""

import pytest
import pandas as pd

from quotes.quote_engine import retrieve_quote
from quotes.quote import Quote


@pytest.fixture
def response():
    """
    Pytest fixture that reads in a fixed quote instance.
    """
    quotes_file = pd.read_csv('./resources/quotes/musk_quotes.csv',sep='\t')
    quote = quotes_file.iloc[12]['quote']
    return quote

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
    assert retrieve_quote(nr=12).return_quote() == "Elon Musk: Any product that needs a manual to work is broken."