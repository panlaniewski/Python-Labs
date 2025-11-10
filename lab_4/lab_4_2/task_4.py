from scipy import integrate
#Определённый интеграл
def definite_integral_func(x):
    return 1 / ((x + 1) * (x ** 2 + 1) ** (1 / 2))

print("Введите пределы для определённого интеграла:")
a = float(input("a: "))
b = float(input("b: "))

def_result = integrate.quad(definite_integral_func, a, b)
print(f"Результет вычисления определённого интеграла от {a} до {b}: {def_result[0]}")
# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
#Двойной интеграл
def double_integral_func(x, y):
    return x * y

print("Введите пределы по y для двойного интеграла:")
y1 = float(input("y1: "))
y2 = float(input("y2: "))

dbl_result = integrate.dblquad(double_integral_func, y1, y2, lambda x: 0, lambda x: 1-2*x)
print(f"Результет вычисления двойного интеграла интеграла: {dbl_result[0]}")