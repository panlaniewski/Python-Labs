import numpy as np

expenses = np.array([56.90, 50.20, 49.20, 46.70, 42.10, 51.20, 59.80, 62.50, 55.80, 56.30, 53.90, 60.40])
month_dict = {
    1: "январь",
    2: "февраль",
    3: "март",
    4: "апрель",
    5: "май",
    6: "июнь",
    7: "июль",
    8: "август",
    9: "сентябрь",
    10: "октябрь",
    11: "ноябрь",
    12: "декабрь",
}

winter_index = [0, 1, 11]
summer_index = [5, 6, 7]
winter_expenses = expenses[winter_index]
summer_expenses = expenses[summer_index]

winter_sum = np.sum(winter_expenses)
print("Сумма расходов зимой:", winter_sum, "BYN")
summer_sum = np.sum(summer_expenses)
print("Сумма расходов летом:", summer_sum, "BYN")

if winter_sum > summer_sum:
    print("В зимний период расходы больше")
elif winter_sum == summer_sum:
    print("В зимний и летний периоды расходы равны")
else:
    print("В летний период расходы больше")
    
max_expenses = np.max(expenses)
max_month = np.where(expenses  == max_expenses)[0] + 1
print(f"Максимальная сумма расходов за весь год: {max_expenses} BYN. Месяц: {month_dict[max_month[0]]}")