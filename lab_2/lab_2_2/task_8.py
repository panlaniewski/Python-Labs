from time import time

def timing(func):
    def wrapper(*args, **kwargs):
        time_start = time()
        res = func(*args, **kwargs)
        time_end = time()
        work_time = (time_end - time_start) * 1000
        print("Время выполнения функции:", work_time, "мс")
        return res
    return wrapper

@timing
def test_loop(n):
    i = 0
    for _ in range(n):
        i += 1
    return i

print(test_loop(10))
print(test_loop(1000000))