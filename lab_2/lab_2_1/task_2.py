user_list = input("Введите последовательность чисел (целых, дробных): ")

num_list = [float(x) if "." in x else int(x) for x in user_list.split()]
   
unique_list = [num for num in num_list if num_list.count(num) == 1]

set_list = list(set(num_list))

repeating_list = [num for num in set_list if num_list.count(num) > 1 and num not in unique_list] 

even_list = [num for num in set_list if isinstance(num, int) and num % 2 == 0]

odd_list = [num for num in set_list if isinstance(num, int) and num % 2 == 1]

negative_list = [num for num in set_list if num < 0]

float_list = [num for num in set_list if isinstance(num, float)]

sum_of_five = sum(num for num in set_list if isinstance(num, int) and num % 5 == 0)
       
# for num in num_list:
#     if num_list.count(num) == 1:
#         unique_list.append(num)
        
# for num in set_list:
#     if set_list.count(num) > 1 and num not in unique_list:
#         repeating_list.append(num)
#     if isinstance(num, int):
#         if num % 2 == 0:
#             even_list.append(num)
#         elif num % 2 == 1:
#             odd_list.append(num)
#         if num % 5 == 0:
#             sum_of_five += num
#     if num < 0:
#         negative_list.append(num)
#     if isinstance(num, float):
#         float_list.append(num) 
    
print("Список пользователя:", num_list)        
print("Уникальные числа:", unique_list)
print("Повторяющиеся числа:", repeating_list)
print("Чётные числа:", even_list)
print("Нечётные числа:", odd_list)
print("Отрицательные числа:", negative_list)
print("Числа с плавающей точкой:", float_list)
print("Сумму всех чисел, кратных 5:", sum_of_five)
print("Самое большое число:", max(num_list))
print("Самое маленькое число:", min(num_list))
