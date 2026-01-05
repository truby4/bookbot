def count_words(text: str):
    lst = text.split()
    count = 0
    for _ in lst:
        count += 1
    return count


def count_characters(text: str):
    dict = {}
    for char in text:
        char = char.lower()
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict


def sorted_dict(dict):
    lst = []
    for char, num in dict.items():
        if char.isalpha():
            lst.append({"char": char, "num": num})
    return sorted(lst, key=lambda d: sorted(d.items()))
