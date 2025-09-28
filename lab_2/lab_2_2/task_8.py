from time import time

def timing(func):
    def wrapper(*args, **kwargs):
        time_start = time()
        res = func(*args, **kwargs)
        time_end = time()
        work_time = time_end - time_start
        print("Время выполнения функции (в мс):", work_time)
        return res
    return wrapper

@timing
def get_loop(n):
    i = 0
    for _ in range(n):
        i += 1
    return i

print(get_loop(10))
print(get_loop(100000000))