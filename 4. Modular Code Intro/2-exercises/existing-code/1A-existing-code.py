file_path = 'data/pride.txt'

with open(file_path, 'r') as f:
    string = f.read()

count_word = string.split().count(word)
count_word_in_text = (word, count_word)

print(count_word_in_text)