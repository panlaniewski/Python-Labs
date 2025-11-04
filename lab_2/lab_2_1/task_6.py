user_list = input("Введите список элементов: ").lower().split()

# for item in user_list:
#     if user_list.count(item) > 1:
#         user_list.pop(user_list.index(item))
        
# print(user_list)

result_list = []
for item in user_list:
    if item not in result_list:
        result_list.append(item)

print(result_list)