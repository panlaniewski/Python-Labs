import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

ticket_sales = pd.read_excel("s7_dataset.xlsx", sheet_name=0)
aiports_codes = pd.read_csv("airports.txt", header=None,
                       names=['id', 'name', 'city', 'country', 'IATA', 'ICAO',
                              'lat', 'lon', 'altitude', 'timezone', 'DST', 'tz_db', 'type', 'source'])
# ------------------------------------------------------------------------------------------------------------------
sns.histplot(ticket_sales['REVENUE_AMOUNT'], bins=100, color="skyblue")
plt.title('Распределение суммы покупки')
plt.xlabel('Сумма')
plt.ylabel('Количество билетов')
plt.show()
# -----------------------------------------------------------------------------------------------------------------
fop_codes = {
    "AH": "оплата по инвойсу",
    "AI": "оплата по инвойсу",
    "BN": "бонусы",
    "CA": "наличные",
    "CC": "кредитная карта",
    "DP": "динамическое ценообразование",
    "EX": "-",
    "FF": "оплата милями",
    "FS": "частично милями",
    "IN": "оплата по инвойсу",
    "LS": "скидка 10%",
    "MC": "-",
    "PS": "подарок",
    "VO": "ваучер",
}

ticket_sales['FOP_TYPE_CODE'] = ticket_sales['FOP_TYPE_CODE'].str.split(',')
fop_type_date = ticket_sales.explode('FOP_TYPE_CODE')['FOP_TYPE_CODE'].str.strip().map(fop_codes)

plt.figure(figsize=(10,6))
sns.countplot(x=fop_type_date, palette='Set2')
plt.title('Частота использования способов оплаты')
plt.xlabel('Способ оплаты')
plt.ylabel('Количество продаж')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
# -----------------------------------------------------------------------------------------------------------------
ticket_sales['ISSUE_DATE'] = pd.to_datetime(ticket_sales['ISSUE_DATE'])
ticket_sales['FLIGHT_DATE_LOC'] = pd.to_datetime(ticket_sales['FLIGHT_DATE_LOC'])

sales_by_date = ticket_sales.groupby(ticket_sales['ISSUE_DATE'].dt.to_period('M'))['REVENUE_AMOUNT'].sum()
sns.barplot(sales_by_date)
plt.title('Суммарная выручка по месяцам')
plt.ylabel('Выручка')
plt.xlabel("")
plt.xticks(rotation=45, ha='right')
plt.show()
# -----------------------------------------------------------------------------------------------------------------
ticket_sales = (
    ticket_sales.merge(aiports_codes[['IATA', 'city', 'country', 'lat', 'lon']], left_on='ORIG_CITY_CODE', right_on='IATA', how='left')
    .rename(columns={'city': 'orig_city', 'country': 'orig_country', 'lat': 'orig_lat', 'lon': 'orig_lon'})
    .drop(columns=['IATA'])
)   
ticket_sales = (
    ticket_sales.merge(aiports_codes[['IATA', 'city', 'country', 'lat', 'lon']], left_on='DEST_CITY_CODE', right_on='IATA', how='left') 
    .rename(columns={'city': 'dest_city', 'country': 'dest_country', 'lat': 'dest_lat', 'lon': 'dest_lon'})
    .drop(columns=['IATA'])
)

aiports_stat = ticket_sales['orig_city'].value_counts().head(10)
sns.barplot(aiports_stat, palette="Set2")
plt.ylabel('Количество рейсов')
plt.xticks(rotation=30, ha='right')
plt.show()
# -----------------------------------------------------------------------------------------------------------------
ticket_sales['ISSUE_DATE'] = pd.to_datetime(ticket_sales['ISSUE_DATE'])
ticket_sales['month'] = ticket_sales['ISSUE_DATE'].dt.month
ticket_sales['year'] = ticket_sales['ISSUE_DATE'].dt.year
ticket_sales['month_name'] = ticket_sales['ISSUE_DATE'].dt.strftime('%b')

monthly_sales = (
    ticket_sales.groupby('month_name').size()
    .reindex(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
)

plt.figure(figsize=(10,5))
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o', linewidth=2, color="green", alpha=0.7)
plt.title('Сезонность продаж авиабилетов')
plt.xlabel('Месяц')
plt.ylabel('Количество билетов')
plt.grid(True, alpha=0.3)
plt.show()
# -----------------------------------------------------------------------------------------------------------------
passengers_codes = {
    "AD": "Взрослый",
    "CHD": "Ребёнок",
    "INF": "Неизвестно",
    "FIM": "Семья",
}

passengers_data = ticket_sales['PAX_TYPE'].map(passengers_codes)

plt.figure(figsize=(8,5))
ax = sns.countplot(x=passengers_data, data=ticket_sales, palette='viridis')
plt.title('Количество продаж по типам пассажиров')
plt.xlabel('Тип пассажира')
plt.ylabel('Количество билетов')

for p in ax.patches:
    ax.text(p.get_x() + p.get_width()/2, p.get_height() + 3,
            int(p.get_height()), ha='center', va='bottom', fontsize=9)
    
plt.tight_layout()
plt.show()
# -----------------------------------------------------------------------------------------------------------------
fop_codes = {
    "AH": "оплата по инвойсу",
    "AI": "оплата по инвойсу",
    "BN": "бонусы",
    "CA": "наличные",
    "CC": "кредитная карта",
    "DP": "динамическое ценообразование",
    "EX": "-",
    "FF": "оплата милями",
    "FS": "частично милями",
    "IN": "оплата по инвойсу",
    "LS": "скидка 10%",
    "MC": "-",
    "PS": "подарок",
    "VO": "ваучер",
}

ticket_sales['FOP_TYPE_CODE'] = ticket_sales['FOP_TYPE_CODE'].str.split(',')
ticket_sales = ticket_sales.explode('FOP_TYPE_CODE')
ticket_sales['FOP_TYPE_CODE'] = ticket_sales['FOP_TYPE_CODE'].str.strip().map(fop_codes)

avg_price_by_fop = (ticket_sales
                    .groupby('FOP_TYPE_CODE')['REVENUE_AMOUNT']
                    .mean()
                    .sort_values(ascending=False))

avg_price_by_fop.plot(kind='bar', figsize=(10,5), title='Средняя стоимость билета по способу оплаты')
plt.ylabel('Средняя сумма, ₽')
plt.xticks(rotation=15, ha='right')
plt.show()
# -----------------------------------------------------------------------------------------------------------------
ticket_sales['ISSUE_DATE'] = pd.to_datetime(ticket_sales['ISSUE_DATE'])

daily_sales = ticket_sales.groupby('ISSUE_DATE').size().rename('tickets_sold').reset_index()
daily_sales.set_index('ISSUE_DATE', inplace=True)

model = ExponentialSmoothing(daily_sales['tickets_sold'], trend='add', seasonal='add', seasonal_periods=30)
forecast = model.fit().forecast(30)

plt.figure(figsize=(12,6))
plt.plot(daily_sales.index, daily_sales['tickets_sold'], label='Фактические продажи')
plt.plot(forecast.index, forecast, label='Прогноз', color='red')
plt.title('Прогноз продаж билетов на 30 дней')
plt.xlabel('Дата')
plt.ylabel('Количество билетов')
plt.legend()
plt.show()