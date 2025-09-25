user_list = input("Введите последовательность чисел: ")

sorted_list = user_list.split()
sorted_list.sort()
sorted_list.reverse()

print("Второе по величине число в списке:", sorted_list[1])