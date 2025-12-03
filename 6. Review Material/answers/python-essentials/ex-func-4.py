def create_report(string, word_to_count, book_name):
    number_words = count_words(string)
    count_word = count_specific_word(string, word_to_count)
    mean_words = calculate_mean_words(string)[0]
    print(f"The name of the book is {book_name}")
    print(f"The first chapter has {number_words} words")
    print(f"Of these {count_word} of these are the word '{word_to_count}'")
    print(f"Each sentence has {round(mean_words,1)} words on average")

create_report(pride, word_to_count = 'Bennet', book_name = 'Pride and Prejudice')
