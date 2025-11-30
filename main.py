from stats import get_num_words
from stats import get_num_characters
from stats import sort_dictionary

import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        words_count = get_num_words(file_content)
        characters_num = get_num_characters(file_content)
        sorted = sort_dictionary(characters_num)
        #Printing Results
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {words_count} total words")
        print("--------- Character Count -------")
        for i in sorted:
            print(f"{i["char"]}: {i["num"]}")
        print("============= END ===============")
        

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        get_book_text(sys.argv[1])


main()
