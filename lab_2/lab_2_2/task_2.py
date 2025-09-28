dict_a = { 'a': 1, 'b': { 'c': 1, 'f': 4 }, 'g': (1, 2) }
dict_b = { 'd': 1, 'b': { 'c': 2, 'e': 3 } } 

def merge_dicts(dict1: dict, dict2: dict):
    for key, value in dict2.items():
        if key in dict1 and isinstance(dict1[key], dict) and isinstance(value, dict):
            merge_dicts(dict1[key], value)
        else:
            dict1[key] = value

merge_dicts(dict_a, dict_b) 
print(dict_a)