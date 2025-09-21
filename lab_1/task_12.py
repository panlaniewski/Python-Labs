
month_talk = 60
month_sms = 30
month_internet = 1024
month_price = 24.99

add_talk_price = 0.89
add_sms_price = 0.59
add_internet_price = 0.79
tax = 0.02

spent_talk = int(input("Введите количество минут: "))
spent_sms = int(input("Введите количество SMS: "))
spent_internet = int(input("Введите количество МБ: "))

if spent_talk < 0 or spent_sms < 0 or spent_internet < 0:
    print("Ошибка: значения не могут быть отрицательными!")
else:
    extra_minutes = max(0, spent_talk - month_talk)
    extra_sms = max(0, spent_sms - month_sms)
    extra_internet = max(0, spent_internet - month_internet)
    
    extra_minutes_price = extra_minutes * add_talk_price
    extra_sms_price = extra_sms * add_sms_price
    extra_internet_price = extra_internet * add_internet_price
    
    total_price = month_price + extra_minutes_price + extra_sms_price + extra_internet
    total_tax = total_price * tax
    total = total_price + total_tax
    
    print("Базовая стоимость тарифа:", round(month_price, 2), "руб.")
    
    if extra_minutes > 0:
        print("Доп. минуты (", extra_minutes, "):", round(extra_minutes_price, 2), "руб.")
    
    if extra_sms > 0:
        print("Доп. SMS (", extra_sms, "):", round(extra_sms_price, 2), "руб.")
    
    if extra_internet > 0:
        print("Доп. трафик (", extra_internet, "МБ ):", round(extra_internet_price, 2), "руб.")
        
    print("Сумма без налога:", round(total_price, 2), "руб.")
    print("Налог (2%):", round(total_tax, 2), "руб.")
    print("ИТОГО К ОПЛАТЕ:", round(total, 2), "руб.")