print("Введите фамилию, имя и отчество")
#Объясляем переменные с помощью множественно присваивания
surname, name, father_name = input(), input(), input()
#Форматируем и выводим строку в вид ФИО
print(surname.title(), name[0].upper() + ".", father_name[0].upper()  + ".")