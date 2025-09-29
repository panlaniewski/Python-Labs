list_a = [1, 2, 3, 4, 5]
list_b = [2, 4, 9, 11, 14]

def quicksort(list):
    less, equal, greater = [], [], []
    if len(list) > 1:
        pivot = list[0]
        for item in list:
            if item < pivot:
                less.append(item)
            elif item == pivot:
                equal.append(item)
            elif item > pivot:
                greater.append(item)
        return quicksort(less) + equal + quicksort(greater) 
    else:  
        return list
    
def merge_sorted_list(lis1: list, list2: list):
    res_list = lis1 + list2
    return quicksort(res_list)

print(merge_sorted_list(list_a, list_b))
