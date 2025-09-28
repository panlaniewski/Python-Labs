def type_check(*types):
    def dec(func):
        def wrapper(*args, **kwargs):
            try:
                for arg, arg_type in zip(args, types):
                    if not isinstance(arg, arg_type):
                        raise TypeError(f"Ожидался тип {arg_type.__name__}, а получен {type(arg).__name__}")
                return func(*args, **kwargs)
            except TypeError as error:
                return f"Ой, ошибка типов! {error}"
        return wrapper
    return dec

@type_check(int, int)
def add(a, b):
    return a + b

print(add(2, 2))




