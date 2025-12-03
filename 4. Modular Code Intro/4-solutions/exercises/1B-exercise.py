def read_file(file_path):
    with open(file_path, 'r') as f:
        input = f.read()
    return input

def get_mean_words_per_sentence(string):
    num_words_per_sentence = [len(x.split()) for x in string.split('.')]
    return sum(num_words_per_sentence)/len(num_words_per_sentence)


if __name__ == "__main__":
    file_path = input("Type in your file path: ")
    string = read_file(file_path)
    print(get_mean_words_per_sentence(string))