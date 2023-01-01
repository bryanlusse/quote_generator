# Native imports
import random
# Third party imports
import pandas as pd
# Package imports
from quotes.quote import Quote

def retrieve_quote():
    """
    Retrieves a random quote from Elon Musk
    """
    quotes_file = pd.read_csv('./resources/quotes/musk_quotes.csv',sep='\t')

    # Get random quote
    nr = random.randint(0,len(quotes_file)-1)
    random_quote = Quote('Elon Musk',quotes_file.iloc[nr]['quote'])

    return random_quote

if __name__ == '__main__':
    quotes_file = pd.read_csv('./resources/quotes/musk_quotes.csv',sep='\t')
    print(retrieve_quote().return_quote())
    print('Success!')
