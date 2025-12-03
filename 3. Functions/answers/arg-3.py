
import string

def get_letter_from_alph_id(*ids):
    alphabet = string.ascii_lowercase
    return {id: alphabet[id%len(alphabet)-1] for id in ids}

get_letter_from_alph_id(1, 4, 5, 27, 97)