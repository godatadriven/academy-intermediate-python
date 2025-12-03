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
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", 
        default="3-data/frankenstein.txt",
        help="Input the file you would like to work with.", 
        type=str)
    parser.add_argument("--word", 
        default="the",
        help="Word to search for.", 
        type=str)
    parser.add_argument("--case_sensitive", 
        action="store_true",
        help="Whether the search should be case sensitive.")
    return parser.parse_args()

def main():
    args = parse_args()

    string = read_file_as_string(args.input_file)

    words = count_words(string, args.case_sensitive)

    word_frequency = get_word_frequency(words, args.word, args.case_sensitive)

    print(f"The word '{args.word}' appears {word_frequency} times.")

if __name__ == "__main__":
    main()