user_str = input("Введите строку (более 14 символов): ")

if len(user_str) > 14:
    user_str = user_str.replace(" ", "")
    print(user_str[1::2])
else:
    print("Сторока слишком короткая!")