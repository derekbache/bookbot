def get_word_count(string):
    return len(string.split())


def get_count_of_characters(string):
    lower_string = string.lower()
    character_count = {}
    for char in lower_string:
        if char not in character_count:
            character_count[char] = 1
        else:
            character_count[char] += 1
    return character_count


def sort_on(items):
    return items["num"]


def sort_dict_into_list_of_dicts(dict):
    list = []
    for key in dict:
        if key.isalpha():
            list.append({"char": key, "num": dict[key]})

    list.sort(reverse=True, key=sort_on)
    return list
