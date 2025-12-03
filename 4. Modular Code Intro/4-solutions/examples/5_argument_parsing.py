import argparse
from collections import Counter
from packages import read_file_as_string

def get_most_common_words(string, num=1):
    return Counter(string.split()).most_common(num)

def get_first_sentence(string):
    return string.split(".")[0]

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", 
        default="3-data/frankenstein.txt",
        help="Input the file you would like to work with.", 
        type=str)
    parser.add_argument("--most_common_words", 
        default=None,
        help="Return the most common words in the file.", 
        type=int)
    parser.add_argument("--show_first_sentence", 
        action="store_true",
        help="Whether to show the first sentence of the file.")
    parser.add_argument("--skip", 
        default=0,
        help="Skip lines at the beginning of the file.", 
        type=int)
    return parser.parse_args()

def main():
    args = parse_args()
    string = read_file_as_string(args.input_file, args.skip)

    if args.most_common_words:
        words_and_count = get_most_common_words(string,args.most_common_words)
        print(f"The {args.most_common_words} most common word(s) are:")
        for word, occurences in words_and_count:
            print(f"{word} (which appears {occurences} times)")

    if args.show_first_sentence:
        first_line = get_first_sentence(string)
        print(f"The first line of the file is: \n{first_line}")

if __name__ == "__main__":
    main()