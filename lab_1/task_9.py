ip_address = input("Введите IP-адрес: ")
split_address = ip_address.split(".")

if len(split_address) == 4:
    if (
        split_address[0].isdigit() and 0 <= int(split_address[0]) <= 255 and
        split_address[1].isdigit() and 0 <= int(split_address[1]) <= 255 and
        split_address[2].isdigit() and 0 <= int(split_address[2]) <= 255 and
        split_address[3].isdigit() and 0 <= int(split_address[3]) <= 255
    ):
        print("Корректный IP-адрес")
    else:
        print("В вашем адресе есть ошибка:(")
else:
    print("В вашем адресе есть ошибка:(")
# if len(split_address) != 4:
#     print("Похоже, это совсем не IP-адрес:(")
# else:
#     is_valid = True
#     for num in split_address:
#         if not num.isdigit():
#             is_valid = False
#             break
#         elif 0 > int(num) < 255:
#             is_valid = False
#             break
#     if is_valid:
#         print("Ваш IP-адрес верный!")       
#     else:
#         print("В вашем адресе есть ошибка:(")        