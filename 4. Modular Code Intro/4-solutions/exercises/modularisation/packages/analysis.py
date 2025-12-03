from collections import Counter 

def count_num_words(string):
    return len(string.split())

def count_word_in_text(string, word='the'):
    count_word = string.split().count(word)
    return word, count_word

def get_mean_words_per_sentence(string):
    num_words_per_sentence = [len(x) for x in string.split('.')]
    return sum(num_words_per_sentence)/len(num_words_per_sentence)

def get_top_words(string, top=10):
    count_words = Counter(string.lower().split())
    return count_words.most_common(top)