from collections import Counter

def read_file(file_path):
    with open(file_path, 'r') as f:
        input = f.read()
    return input

def get_top_10_words(string):
    count_words = Counter(string.lower().split())
    return count_words.most_common(10)


if __name__ == "__main__":
    file_path = input("Type in your file path: ")
    string = read_file(file_path)
    print(get_top_10_words(string))