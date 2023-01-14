"""Functions are defined to load and retrieve quotes"""

# Native imports
import random
import os
import importlib.resources
import glob
# Third party imports
import pandas as pd
# Package imports
from quote_gen.quotes.quote import Quote

namelist = ['Conor Mcgregor', 'Elon Musk']

def load_quotes() -> pd.DataFrame:
    """
    Loads all quotes that are stored in the resources/quotes folder.

    :return: merged_df: Dataframe containing all quotes.
    """
    merged_df = pd.DataFrame()
    resources_path = str(importlib.resources.files('quote_gen.resources.quotes'))

    for i, file in enumerate(sorted(glob.glob(os.path.join(resources_path,'*.csv')))):
        tmp_df = pd.read_csv(os.path.join(resources_path, file), sep='\t')
        tmp_df['author'] = namelist[i]
        merged_df = pd.concat([merged_df, tmp_df])
    return merged_df


def retrieve_quote(number=None) -> Quote:
    """
    Retrieves a random quote from a group of quotees.

    :param int number: Whether the retrieved quote should be random or not.
                       If not random, the number defines the quote to be
                       retrieved.
    :return: a Quote object
    """
    quotes_df = load_quotes()
    if number is None:
        # Get random quote
        number = random.randint(0,len(quotes_df)-1)
        quote = Quote(quotes_df.iloc[number]['author'],
                      quotes_df.iloc[number]['quote'])
    else:
        # Get specified quote
        quote = Quote(quotes_df.iloc[number]['author'],
                      quotes_df.iloc[number]['quote'])
    return quote

if __name__ == '__main__':
    print(retrieve_quote().return_quote())
    print('Success!')
