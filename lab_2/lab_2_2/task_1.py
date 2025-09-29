list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]

def flatten_list(lst: list):
    index = 0
    while index < len(lst):
        if isinstance(lst[index], list):
            sublist = flatten_list(lst[index])
            lst.pop(index)
            for item in sublist:
                lst.insert(index, item)
            index += len(sublist)
        else:
            index += 1
    return lst   

print(flatten_list(list_a))