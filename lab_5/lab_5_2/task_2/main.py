
def unique_elements(lst):
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
