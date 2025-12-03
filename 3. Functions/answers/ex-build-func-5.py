
def combine_first_letters(sentence):
    words = sentence.split()
    new_word=""
    
    for word in words:
        new_word+=word[0]
        
    return new_word

combine_first_letters('this is my example sentence')
