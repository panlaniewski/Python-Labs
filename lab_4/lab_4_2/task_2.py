import numpy as np

user_distances = input("Введите длины участков: ").split(" ")
user_speed = input("Введите скорости на кажом из участков: ").split(" ")

distances = np.array([int(x) for x in user_distances])
speed = np.array([int(x) for x in user_speed])

start_k = int(input("Введите номер начального участка: ")) 
end_p = int(input("Введите номер конечного участка: ")) + 1

full_way = np.sum(distances[start_k:end_p])
full_time = np.sum(distances[start_k:end_p] / speed[start_k:end_p]).round(2)
average_speed = np.mean(speed[start_k:end_p])

print(f"S = {full_way} км, T = {full_time} часа, V = {average_speed} км/ч")