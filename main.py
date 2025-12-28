import sys
from stats import get_word_count, get_count_of_characters, sort_dict_into_list_of_dicts


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book = get_book_text(file_path)
    num_words = get_word_count(book)
    num_characters = get_count_of_characters(book)
    sorted_list = sort_dict_into_list_of_dicts(num_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
