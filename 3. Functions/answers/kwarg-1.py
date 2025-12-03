def get_full_name(**names):
    for key, value in names.items():
        print(f"{key.replace('_',' ').capitalize()}: {value}")

get_full_name(first_name='Peter', last_name='Parker')