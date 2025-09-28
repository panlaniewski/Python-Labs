list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2 ,3]]]]

def unique_elements(lst: list):
    index = 0
    while index < len(lst):
        if isinstance(lst[index], list):
            sublist = unique_elements(lst[index])
            lst.pop(index)
            for item in sublist:
                lst.insert(index, item)
            index += len(sublist)
        else:
            index += 1
    return list(set(lst))  

print(unique_elements(list_a)) 