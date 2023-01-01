"""Main module."""

from fastapi import FastAPI
from quotes.quote_engine import retrieve_quote

app = FastAPI()

@app.get("/")
def root():
    """
    docstring
    """
    return {"message": "Hello and welcome to the quote API"}

@app.get("/get_quote")
def get_quote():
    """
    docstring
    """
    retrieved_quote = retrieve_quote()
    return {"message": retrieved_quote.return_quote()}


if __name__ == "__main__":
    get_quote()
    print('Success')
