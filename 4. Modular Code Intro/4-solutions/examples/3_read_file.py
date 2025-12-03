def read_file_as_string(file_path):
    with open(file_path, 'r') as f:
        string = f.read()
    return string

def count_num_words(string):
    return len(string.split())


def main():
    file_path = input("Type in your file path: ")
    string = read_file_as_string(file_path)
    num_words = count_num_words(string)
    print(f"The number of words in {file_path} is {num_words}")


if __name__ == "__main__":
    main()