print("Введите сумму (рубли):")

money = int(input())

one_hundred = money // 100
money %= 100
fifty = money // 50
money %= 50
ten = money // 10
money %= 10
five = money // 5
money %= 5
two = money // 2
money %= 2
one = money

print("Купюр по 100 рублей:", one_hundred)
print("Купюр по 50 рублей:", fifty)
print("Купюр по 10 рублей:", ten)
print("Купюр по 5 рублей:", five)
print("Монет по 2 рубля:", two)
print("Монет по 1 рублю:", one)