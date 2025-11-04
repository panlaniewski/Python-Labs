user_set_1 = set(input("Введите первую последовательность: ").split())
user_set_2 = set(input("Введите вторую последовательность: ").split())

common_set = user_set_1 & user_set_2
print("Числа, которые присутствуют в обоих наборах:", common_set)

only_first = user_set_1 - user_set_2
print("Числа из первого, которых нет во втором:", only_first)

only_second = user_set_2 - user_set_1
print("Числа из второго, которых нет в первом:", only_second)

symmetric_set = user_set_1 ^ user_set_2
print("Числа из обоих наборов, кроме тех, что совпали:", symmetric_set)