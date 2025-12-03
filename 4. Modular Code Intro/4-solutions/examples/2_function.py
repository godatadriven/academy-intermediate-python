def count_num_words(string):
    return len(string.split())

def main():
    string = input("Type in your string")
    num_words = count_num_words(string)
    print(num_words)

# Add this - 
if __name__ == "__main__":
    main()