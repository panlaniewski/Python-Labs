import numpy as np

user_distances = input("Введите длины участков: ").split(" ")
user_speed = input("Введите скорости на каждом из участков: ").split(" ")

distances = np.array(user_distances).astype(np.float64)
speed = np.array(user_speed).astype(np.float64)

k = int(input("Введите номер начального участка: ")) 
p = int(input("Введите номер конечного участка: ")) 

if distances.size == speed.size and k >= 1 and p >= k and p <= distances.size:
    selected_distances = distances[k:p+1]
    selected_speeds = speed[k:p+1]
    
    full_way = np.sum(selected_distances)
    full_time = np.sum(selected_distances / selected_speeds)
    average_speed = full_way / full_time
    
    print(f"S = {full_way} км, T = {full_time:.2f} час, V = {average_speed:.2f} км/ч")
else:
    print("Некоторые введённые данные не корректны!")