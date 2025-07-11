from stats import number_of_words
from stats import counting_characters
from stats import sorted_dictionary
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

with open(book_path, "r") as f:
    text = f.read()

def main():

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_text = get_book_text(book_path)
    character_frequencies = counting_characters(get_text)
    count = number_of_words(get_text)
    print("Found "f"{count} total words")
    print("--------- Character Count -------")
    # print(character_frequencies)
    sorted_characters_in_dictionary = sorted_dictionary(character_frequencies)
    for entry in sorted_characters_in_dictionary:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

main()

