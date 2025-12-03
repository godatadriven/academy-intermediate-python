from packages import read_file_as_string
from packages import count_num_words

def main():
    file_path = input("Type in your file path: ")
    string = read_file_as_string(file_path)
    num_words = count_num_words(string)
    print(f"The number of words in {file_path} is {num_words}")


if __name__ == "__main__":
    main()