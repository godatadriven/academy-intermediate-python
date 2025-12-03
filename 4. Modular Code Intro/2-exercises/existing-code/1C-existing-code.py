from collections import Counter

file_path = input('File path: ')

with open(file_path, 'r') as f:
    input = f.read()

count_words = Counter(string.lower().split())

most_common_words = count_words.most_common(10)

print(most_common_words)
