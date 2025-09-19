print("Введите фамилию, имя и отчество")

surname, name, father_name = input(), input(), input()

print(surname[0].upper() + surname[1:], name[0].upper() + ".", father_name[0].upper()  + ".")