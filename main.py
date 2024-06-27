
def main():
    book_path = "books/frankenstein.txt" 
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    print_report(word_count, character_count)


def get_book_text(path):
    with open(path) as file:
        text = file.read()
    return text

def get_word_count(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def get_character_count(text):
    count = {}
    text = text.lower()
    text = ''.join(e for e in text if e.isalpha())
    for char in text:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    list_of_dicts = []
    for key, value in count.items():
        list_of_dicts.append({"char": key, "num": value})

    sorted_list = sorted(list_of_dicts, reverse=True, key=sort_on)

    return sorted_list

def print_report(word_count, character_count):
    print("~~~~~ Report of books/frankenstein.txt ~~~~~")
    print()
    print(f"The book has {word_count} words.")
    print()
    print("The most common characters are:")
    for i in range(len(character_count)):
        print(f"{character_count[i]['char']}: {character_count[i]['num']}")
    print()
    print("~~~~~ End of report ~~~~~")
    print()

main()