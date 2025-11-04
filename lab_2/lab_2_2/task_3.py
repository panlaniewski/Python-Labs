import time

def log_calls(path):
    def dec(func):
        def wrapper(*args, **kwargs):
            call_time = time.strftime("%Y-%m-%d %H:%M:%S")
            try:
                res = func(*args, **kwargs)
                with open(path, "a", encoding="utf-8") as file:
                    file.write(f"Время вызова: {call_time}, имя функции: {func.__name__}, вызвана с args={args}, kwargs={kwargs}")
            except:
                print("Ошибка файла!")
            return res
        return wrapper
    return dec

@log_calls("log_calls_task_3.txt")
def say_hi(str):
    print("Hello,", str)
    
say_hi("World")