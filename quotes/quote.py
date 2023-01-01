# The quote class which holds information about the quote and the person who said it
class Quote:
 
    # init method or constructor
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote
 
    # Sample Method
    def return_quote(self):
        """
        Returns the quote as a string object

        :return: The quote 
        """
        return f'{self.author}: {self.quote}'

if __name__ == '__main__':
    test = Quote('Elon Musk', 'This is a test quote')
    print(test.return_quote())
    print('Success')