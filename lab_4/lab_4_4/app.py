import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
# ------------------------------------------------------------------------------------------------------------------
ticket_sales = pd.read_excel("s7_dataset.xlsx", sheet_name=0)
aiports_codes = pd.read_csv("airports.txt", 
                            header=None,
                            names=['id', 'name', 'city', 'country', 'IATA', 'ICAO', 'lat', 
                                   'lon', 'altitude', 'timezone', 'DST', 'tz_db', 'type', 'source']
                            )
# ------------------------------------------------------------------------------------------------------------------
FOP_CODES = {
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
    "VO": "ваучер"
}
PASSENGER_CODES = {
    "AD": "Взрослый", "CHD": "Ребёнок", "INF": "Неизвестно", "FIM": "Семья"
}
MONTH_NAMES = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

def set_plot_settings(title, xlabel, ylabel, rotation=0):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if rotation:
        plt.xticks(rotation=rotation, ha='right')
    plt.tight_layout()
    plt.show()
# ------------------------------------------------------------------------------------------------------------------
plt.figure(figsize=(10, 6))
sns.histplot(ticket_sales['REVENUE_AMOUNT'], bins=100, color="skyblue")
set_plot_settings('Распределение суммы покупки', 'Сумма', 'Количество билетов')
# ------------------------------------------------------------------------------------------------------------------
fop_types_data = (
    ticket_sales['FOP_TYPE_CODE']
    .str.split(',')
    .explode('FOP_TYPE_CODE')
    .str.strip()
    .map(FOP_CODES)
)
plt.figure(figsize=(10, 6))
sns.countplot(x=fop_types_data, palette='Set2')
set_plot_settings('Частота использования способов оплаты', 'Способ оплаты', 'Количество продаж', rotation=45)
# -----------------------------------------------------------------------------------------------------------------
ticket_sales['ISSUE_DATE'] = pd.to_datetime(ticket_sales['ISSUE_DATE'])
sales_by_date = ticket_sales.groupby(ticket_sales['ISSUE_DATE'].dt.to_period('M'))['REVENUE_AMOUNT'].sum()

plt.figure(figsize=(12, 6))
sns.barplot(x=sales_by_date.index.astype(str), y=sales_by_date.values)
set_plot_settings('Суммарная выручка по месяцам', '', 'Выручка', rotation=45)
# -----------------------------------------------------------------------------------------------------------------
ticket_sales_airports = (
    ticket_sales.merge(aiports_codes[['IATA', 'city', 'country', 'lat', 'lon']], 
           left_on='ORIG_CITY_CODE', right_on='IATA', how='left')
    .rename(columns={'city': 'orig_city', 'country': 'orig_country', 'lat': 'orig_lat', 'lon': 'orig_lon'})
    .drop(columns=['IATA'])
)
airports_stat = ticket_sales_airports['orig_city'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=airports_stat.index, y=airports_stat.values, palette="Set2")
set_plot_settings('Топ-10 городов отправления', 'Город', 'Количество рейсов', rotation=30)
# -----------------------------------------------------------------------------------------------------------------
ticket_sales['month_name'] = ticket_sales['ISSUE_DATE'].dt.strftime('%b')
monthly_sales = ticket_sales.groupby('month_name').size().reindex(MONTH_NAMES)

plt.figure(figsize=(10, 5))
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, 
             marker='o', linewidth=2, color="green", alpha=0.7)
plt.grid(True, alpha=0.3)
set_plot_settings('Сезонность продаж авиабилетов', 'Месяц', 'Количество билетов')
# -----------------------------------------------------------------------------------------------------------------
passengers_data = ticket_sales['PAX_TYPE'].map(PASSENGER_CODES)

plt.figure(figsize=(8, 5))
ax = sns.countplot(x=passengers_data, palette='viridis')

for p in ax.patches:
    ax.text(p.get_x() + p.get_width() / 2, p.get_height() + 3,
            int(p.get_height()), ha='center', va='bottom', fontsize=9)
    
set_plot_settings('Количество продаж по типам пассажиров', 'Тип пассажира', 'Количество билетов')
# -----------------------------------------------------------------------------------------------------------------
ticket_sales_fop = ticket_sales.copy()
ticket_sales_fop['FOP_TYPE_CODE'] = ticket_sales_fop['FOP_TYPE_CODE'].str.split(',')
ticket_sales_fop = ticket_sales_fop.explode('FOP_TYPE_CODE')
ticket_sales_fop['FOP_TYPE_CODE'] = ticket_sales_fop['FOP_TYPE_CODE'].str.strip().map(FOP_CODES)

avg_price_by_fop = (
    ticket_sales_fop.groupby('FOP_TYPE_CODE')['REVENUE_AMOUNT']
    .mean()
    .sort_values(ascending=False))

plt.figure(figsize=(10, 5))
sns.barplot(avg_price_by_fop)
set_plot_settings('Средняя стоимость билета по способу оплаты', 'Способ оплаты', 'Средняя сумма', rotation=15)
# -----------------------------------------------------------------------------------------------------------------
daily_sales = ticket_sales.groupby('ISSUE_DATE').size().rename('tickets_sold').reset_index()
daily_sales.set_index('ISSUE_DATE', inplace=True)

model = ExponentialSmoothing(daily_sales['tickets_sold'], trend='add', seasonal='add', seasonal_periods=30)
forecast = model.fit().forecast(30)

plt.figure(figsize=(12, 6))
plt.plot(daily_sales.index, daily_sales['tickets_sold'], label='Фактические продажи')
plt.plot(forecast.index, forecast, label='Прогноз', color='red')
set_plot_settings('Прогноз продаж билетов на 30 дней', 'Дата', 'Количество билетов')