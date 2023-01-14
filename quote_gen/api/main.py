"""Main module."""

from fastapi import FastAPI
from quote_gen.quotes.quote_engine import retrieve_quote

app = FastAPI()

@app.get("/")
def root():
    """
    Default get request.
    #TODO Create simple landing page
    """
    return {"message": "Hello and welcome to the quote API"}

@app.get("/get_quote")
def get_quote():
    """
    Gets a random quote.

    :return: a message containing a string with the
             quote and the person it was said by.
    """
    retrieved_quote = retrieve_quote()
    return {"message": retrieved_quote.return_quote()}


if __name__ == "__main__":
    get_quote()
    print('Success!')
