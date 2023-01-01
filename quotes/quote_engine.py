# Native imports
import random
# Third party imports
import pandas as pd
# Package imports
from quotes.quote import Quote

def retrieve_quote(nr=None):
    """
    Retrieves a random quote from Elon Musk.

    :param int nr: Whether the retrieved quote should be random or not.
                   If not random, the number defines the quote to be
                   retrieved.
    :return: a Quote object
    """
    quotes_file = pd.read_csv('./resources/quotes/musk_quotes.csv',sep='\t')
    if nr is None:
        # Get random quote
        nr = random.randint(0,len(quotes_file)-1)
        quote = Quote('Elon Musk',quotes_file.iloc[nr]['quote'])
    else:
        # Get specified quote
        quote = Quote('Elon Musk',quotes_file.iloc[nr]['quote'])
    return quote

if __name__ == '__main__':
    quotes_file = pd.read_csv('./resources/quotes/musk_quotes.csv',sep='\t')
    print(retrieve_quote().return_quote())
    print('Success!')
