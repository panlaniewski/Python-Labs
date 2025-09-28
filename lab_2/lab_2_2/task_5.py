def cache(func):
    cache_dict = {}
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache_dict:
            print("Взято из кэша")
            return cache_dict[key]
        else:
            print("Вычисляем впервые")   
            res = func(*args, **kwargs)
            cache_dict[key] = res
            return res
    return wrapper

@cache
def get_sum(a, b):
    return a + b

@cache
def get_prod(a, b):
    return a * b

print(get_sum(3, 2)) 
print(get_prod(3, 2))
print(get_sum(3, 2)) 