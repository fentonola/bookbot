def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    count_dict = {}
    for character in text:
        char = character.lower()
        if char not in count_dict:
            count_dict[char] = 1
        else:
            count_dict[char] += 1
    return count_dict

def sort_by(dict):
    return dict['num']

def sort_dicts(dictionary):
    sorted_list = []
    for char, num in dictionary.items():
        mini_dict = {}
        mini_dict['char'] = char
        mini_dict['num'] = num
        sorted_list.append(mini_dict)
    sorted_list.sort(reverse=True, key=sort_by)
    return sorted_list
    
