dict_a = { 'a': 3, 'b': { 'c': 1, 'f': 4 } }
dict_b = { 'a': 4, 'd': 1, 'b': { 'c': 2, 'e': 3 } } 

def merge_dicts(dict1: dict, dict2: dict):
    for key, value in dict2.items():
        if key in dict1:
            if isinstance(dict1[key], dict) and isinstance(value, dict):
                merge_dicts(dict1[key], value)
            elif isinstance(dict1[key], (int, float)) and isinstance(value, (int, float)):
                dict1[key] = max(dict1[key], value)
            else:
                dict1[key] = [dict1[key], value]
        else:
            dict1[key] = value
            
merge_dicts(dict_a, dict_b) 
print(dict_a)