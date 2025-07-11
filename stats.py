def number_of_words(text):
    num_words = text.split()
    count = len(num_words)
    return count

def counting_characters(text):
    num_characters = text.lower()
    character_dictionary = {}
    for character in num_characters:
        if character in character_dictionary:
            current_count = character_dictionary[character]
            new_count = current_count + 1
            character_dictionary[character] = new_count
        else:
            character_dictionary[character] = 1
    return character_dictionary

def sorted_dictionary(character_dictionary):
    empty_list = []
    for char, num in character_dictionary.items():
        new_dict = {"char": char, "num": num}
        empty_list.append(new_dict)
    empty_list.sort(reverse=True, key=sort_on)
    return empty_list

def sort_on(dict_items):
    return dict_items["num"]





