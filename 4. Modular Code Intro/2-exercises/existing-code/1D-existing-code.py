import argparse
from collections import Counter


def read_file_as_string(file_path):
    with open(file_path, 'r') as f:
        string = f.read()
    return string

def count_words(string, case_sensitive):
    if not case_sensitive:
        string = string.lower()
    return Counter(string.split())

def get_word_frequency(counted_words,word, case_sensitive):
    if not case_sensitive:
        word = word.lower()
    return counted_words[word]

def parse_args():
    #TODO
    pass

def main():
    #TODO
    pass

if __name__ == "__main__":
    main()