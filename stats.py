def get_num_words(text):
    text_list = text.split()
    total_words = len(text_list)
    return total_words

def get_num_characters(text):
    characters = {}
    for ch in text:
        ch = ch.lower()
        if ch not in characters:
            characters[ch] = 1
        else:
            characters[ch] += 1
    return characters

def sort_order(item):
    return item["num"]

def sort_dictionary(dict):
    characters_list = []
    for char in dict:
        new_dict = {}
        new_dict["char"] = char
        new_dict["num"] = dict[char]
        characters_list.append(new_dict)
    characters_list.sort(key=sort_order, reverse=True)
    return characters_list
