import sys

from stats import count_characters, count_words, sorted_dict


def get_book_text(path: str):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)

    print(f"""============ BOOKBOT ============
    Analyzing book found at {path}...
    ----------- Word Count ----------
    Found {num_words} total words
    --------- Character Count -------""")

    dict = sorted_dict(count_characters(text))
    for item in dict:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
