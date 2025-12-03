
def create_greeting(name='World'):
    """
    takes in a name and returns a string saying "Hello [name]!"
    
    name: str
    """
    return f"Hello, {name}!"


def check_even(a):
    """
    takes in a number, returns a bool indicating whether the number is even or odd. 
    
    a: int or float
    """
    return a % 2 == 0


def combine_first_letters(sentence):
    """
    takes a sentence (string) and combines the first letters of each word into a new word.
    
    sentence : str
    """
    words = sentence.split()
    new_word=""
    
    for word in words:
        new_word+=word[0]
        
    return new_word

