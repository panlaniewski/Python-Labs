print("Введите строку:")

string = input()
formatted_str = string.replace(" ", "").lower()

if formatted_str == formatted_str[::-1]:
    print("Палиндром:", string)