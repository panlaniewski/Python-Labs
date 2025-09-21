from random import randint

rand_num = randint(1, 100)
user_num = 0

while user_num != rand_num:
    user_num = int(input("Введите число от 1 до 100: "))
    
    if user_num < 1 or user_num > 100:
        print("Число должно быть от 1 до 100!")
        continue
    if user_num < rand_num:
        print("Больше")
    elif user_num > rand_num:
        print("Меньше")
    else:
        print("Угадали!")