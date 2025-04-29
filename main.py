
import sys
from stats import get_num_words, get_chars_dict, sort_dicts


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    # 0. Get CLI working
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # 1. Read the file and get the text
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    # 2. Get the word count
    num_words = get_num_words(text)
    # 3. Get the character count
    num_chars = get_chars_dict(text)
    # 4. Get a sorted list of dictionaries
    sorted_chars = sort_dicts(num_chars)
    # 5. Print report
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for char_dict in sorted_chars:
        char = char_dict['char']
        if char.isalpha():
            print(f'{char}: {char_dict['num']}')
    print('============= END ===============')

main()