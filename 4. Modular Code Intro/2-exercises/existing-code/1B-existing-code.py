file_path = input('File path: ')

with open(file_path, 'r') as f:
    string = f.read()

sentences = string.split('.')
num_words_per_sen = [len(sen.split()) for sen in sentences]

mean_num_words = sum(num_words_per_sen)/len(num_words_per_sen)

print(mean_num_words)