from packages.read_book import read_file_as_string
from packages.analysis import count_num_words, count_word_in_text
from packages.analysis import get_mean_words_per_sentence, get_top_words

def main():
    file_path = input("Type in your file path: ")
    
    string = read_file_as_string(file_path)

    num_words = count_num_words(string)
    count_the = count_word_in_text(string)
    mean_per_sen = get_mean_words_per_sentence(string)
    top_5 = get_top_words(string, top=5)

    print(f"\n\033[1;32;40mAnalysis on the book: {file_path}\n\033[0m")
    print(f"The number of words is {num_words}")
    print(f"The number of time 'the' appears is {count_the}")
    print(f"The mean words per sentence is {mean_per_sen}")
    print(f"The top 10 words are {top_5}\n")


if __name__ == "__main__":
    main()