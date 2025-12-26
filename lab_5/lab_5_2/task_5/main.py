
def merge_dicts(dict1: dict, dict2: dict):
    for key, value in dict2.items():
        if key in dict1:
            if isinstance(dict1[key], dict) and isinstance(value, dict):
                merge_dicts(dict1[key], value)
            elif isinstance(dict1[key], (int, float)) and isinstance(value, (int, float)):
                dict1[key] = max(dict1[key], value)
            elif type(value) is not type(dict1[key]):
                dict1[key] = [dict1[key], value]
            else:
                dict1[key] = value 
        else:
            dict1[key] = value