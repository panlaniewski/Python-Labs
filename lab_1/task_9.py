print("Введите IP-адрес:")
ip_address = input()
split_address = ip_address.split(".")

if len(split_address) != 4:
    print("Похоже, это совсем не IP-адрес:(")
else:
    is_valid = True
    for num in split_address:
        if not num.isdigit():
            is_valid = False
            break
        elif 0 > int(num) < 255:
            is_valid = False
            break
    if is_valid:
        print("Ваш IP-адрес верный!")       
    else:
        print("В вашем адресе есть ошибка:(")        