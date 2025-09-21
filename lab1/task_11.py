print("Введите дату своего рождения:")

date = input()
month = int(date.split(".")[1])
day = int(date.split(".")[0])

if (day < 1 or day > 31) or (month < 1 or month > 12):
    print("Неверная дата!")
elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
    print("Ваш знак: Овен") 
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    print("Ваш знак: Телец") 
elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
    print("Ваш знак: Близнецы")
elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
    print("Ваш знак: Рак")
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    print("Ваш знак: Лев")
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    print("Ваш знак: Дева")
elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    print("Ваш знак: Весы")
elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    print("Ваш знак: Скорпион")
elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    print("Ваш знак: Стрелец")
elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
    print("Ваш знак: Козерог")
elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
    print("Ваш знак: Водолей")
else:
    print("Ваш знак: Рыбы")