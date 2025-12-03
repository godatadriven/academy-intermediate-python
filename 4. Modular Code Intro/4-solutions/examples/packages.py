def read_file_as_string(file_path):
    with open(file_path, 'r') as f:
        string = f.read()
    return string

def count_num_words(string):
    return len(string.split())