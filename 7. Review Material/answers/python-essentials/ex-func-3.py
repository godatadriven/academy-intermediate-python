def calculate_mean_words(string):
    cleaned_string = (
        string
        .replace('Mr.', 'Mr').replace('Mrs.','Mrs')
        .replace('?', '.').replace('!', '')
    )
    sentences = cleaned_string.split('.')
    words = cleaned_string.split()
    return len(words)/len(sentences), sentences


calculate_mean_words(pride)
