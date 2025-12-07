import numpy as np

expenses = np.array([56.90, 50.20, 49.20, 46.70, 42.10, 51.20, 59.80, 62.50, 55.80, 56.30, 53.90, 60.40])
month_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

winter_index = [0, 1, 11]
summer_index = [5, 6, 7]
winter_expenses = expenses[winter_index]
summer_expenses = expenses[summer_index]

winter_sum = np.sum(winter_expenses)
print("Amount of expenses in winter:", winter_sum, "BYN")
summer_sum = np.sum(summer_expenses)
print("Amount of expenses in summer:", summer_sum, "BYN")

if winter_sum > summer_sum:
    print("During the winter period, expenses are higher")
elif winter_sum == summer_sum:
    print("In winter and summer period expenses are equal")
else:
    print("During the summer period, expenses are higher")
    
max_expenses = np.max(expenses)
max_month = np.where(expenses  == max_expenses)[0] + 1
print(f"Max amount of expenses during this year: {max_expenses} BYN in {month_dict[max_month[0]]}")