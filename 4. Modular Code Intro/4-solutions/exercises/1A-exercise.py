def read_file(file_path):
    with open(file_path, 'r') as f:
        input = f.read()
    return input

def count_word_in_text(string, word='the'):
    count_word = string.split().count(word)
    return word, count_word


if __name__ == "__main__":
    file_path = input("Type in your file path: ")
    string = read_file(file_path)
    print(count_word_in_text(string))