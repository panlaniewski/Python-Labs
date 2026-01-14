import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
# ------------------------------------------------------------------------------------------------------------------
df = pd.read_excel("s7_dataset.xlsx", sheet_name=0)
# ------------------------------------------------------------------------------------------------------------------
FOP_CODES = {
    "AH": "оплата по инвойсу", 
    "AI": "оплата по инвойсу", 
    "BN": "бонусы",
    "CA": "наличные", 
    "CC": "кредитная карта", 
    "DP": "динамическое ценообразование",
    "FF": "оплата милями", 
    "FS": "частично милями", 
    "IN": "оплата по инвойсу", 
    "LS": "скидка 10%", 
    "PS": "подарок", 
    "VO": "ваучер"
}
# ------------------------------------------------------------------------------------------------------------------
PASSENGER_CODES = {
    "AD": "Взрослый", "CHD": "Ребёнок", "INF": "Неизвестно", "FIM": "Семья"
}
# ------------------------------------------------------------------------------------------------------------------
FFP_DICT = {
    'FFP': 'Есть',
    np.nan: 'Отсутствует'
}
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
revenue_amount = df["REVENUE_AMOUNT"]
print(f"Общее число строк в таблице: {revenue_amount.count()}")
print(f"Средняя сумма покупки билетов: {revenue_amount.mean()}")
print(f"Стандартное отклонение суммы покупки билетов: {revenue_amount.std()}")
print(f"Медианное значение суммы покупки билетов: {revenue_amount.median()}")
print(f"Мода суммы покупки билетов: {revenue_amount.mode()[0]}")
print(f"Максимальное значение суммы покупки билетов: {revenue_amount.max()}")
print(f"Минимальное значение суммы покупки билетов: {revenue_amount.min()}")
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
f, axs = plt.subplots(1, 2, figsize=(12, 6))

orig_counts = df['ORIG_CITY_CODE'].value_counts().head(10)
dest_counts = df['DEST_CITY_CODE'].value_counts().head(10)

sns.barplot(x=orig_counts.index, y=orig_counts.values, ax=axs[0])
axs[0].set_title('Топ-10 аэропортов вылета по количеству билетов')
axs[0].set_xlabel('Аэропорт')
axs[0].set_ylabel('Количество билетов')

sns.barplot(x=dest_counts.index, y=dest_counts.values, ax=axs[1])
axs[1].set_title('Топ-10 аэропортов прибывания по количеству билетов')
axs[1].set_xlabel('Аэропорт')
axs[1].set_ylabel('Количество билетов')
plt.show()
# # ------------------------------------------------------------------------------------------------------------------
f, axs = plt.subplots(1, 2, figsize=(12, 6))

revenue_by_orig = df.groupby('ORIG_CITY_CODE')['REVENUE_AMOUNT'].sum().sort_values(ascending=False).head(10)
revenue_by_dest = df.groupby('DEST_CITY_CODE')['REVENUE_AMOUNT'].sum().sort_values(ascending=False).head(10)

sns.barplot(x=revenue_by_orig.index, y=revenue_by_orig.values, ax=axs[0])
axs[0].set_title('Топ-10 аэропортов вылета по выручке')
axs[0].set_xlabel('Аэропорт')
axs[0].set_ylabel('Выручка (мл. у.е.)')

sns.barplot(x=revenue_by_dest.index, y=revenue_by_dest.values, ax=axs[1])
axs[1].set_title('Топ-10 аэропортов прибывания по выручке')
axs[1].set_xlabel('Аэропорт')
axs[1].set_ylabel('Выручка (мл. у.е.)')
plt.show()
# # ------------------------------------------------------------------------------------------------------------------
f, axs = plt.subplots(1, 2, figsize=(12, 6))

avg_price_orig = df.groupby('ORIG_CITY_CODE')['REVENUE_AMOUNT'].mean().sort_values(ascending=False).head(10)
avg_price_dest = df.groupby('DEST_CITY_CODE')['REVENUE_AMOUNT'].mean().sort_values(ascending=False).head(10)

sns.barplot(x=avg_price_orig.index, y=avg_price_orig.values, ax=axs[0])
axs[0].set_title('Топ-10 аэропортов вылета по средней стоимости билетов')
axs[0].set_xlabel('Аэропорт')
axs[0].set_ylabel('Средняя стоимость')

sns.barplot(x=avg_price_dest.index, y=avg_price_dest.values, ax=axs[1])
axs[1].set_title('Топ-10 аэропортов прибывания по средней стоимости билетов')
axs[1].set_xlabel('Аэропорт')
axs[1].set_ylabel('Средняя стоимость')
plt.show()
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
df['FLIGHT_DATE_LOC'] = pd.to_datetime(df['FLIGHT_DATE_LOC'])
df['FLIGHT_YEAR'] = df['FLIGHT_DATE_LOC'].dt.year
fligths_2022 = df[df['FLIGHT_YEAR'] == 2022]
fligths_2022['FLIGHT_MONTH'] = fligths_2022['FLIGHT_DATE_LOC'].dt.month
tickets_by_month = fligths_2022.groupby('FLIGHT_MONTH')["REVENUE_AMOUNT"].agg(["size", "sum", "mean"])

f, axs = plt.subplots(1, 3, figsize=(12, 6))
# ------------------------------------------------------------------------------------------------------------------
sns.lineplot(data=tickets_by_month, x="FLIGHT_MONTH", y="size", marker='o', ax=axs[0])
axs[0].set_title('Динамика количества билетов за 2022 год')
axs[0].set_xlabel('Месяц')
axs[0].set_ylabel('Количество билетов')
axs[0].grid(True, alpha=0.5)
# ------------------------------------------------------------------------------------------------------------------
sns.lineplot(data=tickets_by_month, x="FLIGHT_MONTH", y="sum", marker='o', ax=axs[1], color='orange')
axs[1].set_title('Динамика выручки за 2022 год')
axs[1].set_xlabel('Месяц')
axs[1].set_ylabel('Выручка')
axs[1].grid(True, alpha=0.5)
# ------------------------------------------------------------------------------------------------------------------
sns.lineplot(data=tickets_by_month, x="FLIGHT_MONTH", y="mean", marker='o', ax=axs[2], color="cyan")
axs[2].set_title('Динамика средней стоимости билетов за 2022 год')
axs[2].set_xlabel('Месяц')
axs[2].set_ylabel('Средняя стоимость')
axs[2].grid(True, alpha=0.5)
f.tight_layout()
plt.show()
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
f, axs = plt.subplots(1, 2, figsize=(12, 6))

df['PAX_TYPE'].map(PASSENGER_CODES).value_counts().plot(kind='pie', autopct='%1.1f%%', ax=axs[0])
axs[0].set_title('Распределение типов пассажиров')
axs[0].set_ylabel('')

df['FFP_FLAG'] = df['FFP_FLAG'].map(FFP_DICT)
sns.countplot(df['FFP_FLAG'], color="mediumseagreen", ax=axs[1])
axs[1].set_title('Наличие программы лояльности у пассажиров')
axs[1].set_xlabel("Количество пассажиров")
axs[1].set_xlim(15000, 32500)
axs[1].set_ylabel("")
plt.show()
# ------------------------------------------------------------------------------------------------------------------
df['FOP_TYPE_CODE'] = df['FOP_TYPE_CODE'].map(FOP_CODES).fillna("прочее")
plt.figure(figsize=(12, 6))
sns.barplot(data=df, y='FOP_TYPE_CODE', x='REVENUE_AMOUNT', color='coral')
plt.title("Распределение способов оплаты среди пассажиров")  
plt.xlabel('Цена')
plt.ylabel('Способ оплаты')
plt.tight_layout() 
plt.show()
# ------------------------------------------------------------------------------------------------------------------
df['flight_month'] = df['FLIGHT_DATE_LOC'].dt.month
tickets_by_month = df.groupby('flight_month').size().reset_index(name='tickets')

x = tickets_by_month['flight_month']
y = tickets_by_month['tickets']

slope, intercept, r_value, p_value, std_err = linregress(x, y)
y_trend = intercept + slope * x

next_month = x.max() + 1
forecast = intercept + slope * next_month

plt.plot(x, y, 'o', label='Фактические данные')
plt.plot(x, y_trend, label='Линейный тренд')
plt.scatter(next_month, forecast, marker='x', s=100, label='Прогноз')
plt.xlabel('Месяц')
plt.ylabel('Количество билетов')
plt.title('Аппроксимация количества билетов линейным трендом')
plt.legend()
plt.grid(True)
plt.show()