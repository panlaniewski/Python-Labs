import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import os
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
sales_data = pd.read_excel("sales_data.xlsx", header=1)
sales_data = sales_data.dropna(axis=1, how='all') 
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
sales_data['Год-мес'] = sales_data['Год-мес'].astype(str)
sales_data['Средняя цена'] = sales_data['Продажи'] / sales_data['Количество']
sales_data['Прибыль'] = sales_data['Продажи'] - sales_data['Себестоимость']
sales_data['модель'] = sales_data['товар'].apply(lambda x: x.split(' ')[1].split('-')[0])
#----------------------------------------------------------------------------------------------------------------
overall_monthly = sales_data.groupby('Год-мес').agg({
    'Количество': 'sum',
    'Продажи': 'sum',
    'Себестоимость': 'sum',
    'Прибыль': 'sum',
    'Средняя цена': 'mean'
}).reset_index()
overall_monthly['Год-мес'] = pd.to_datetime(overall_monthly['Год-мес'] + '01', format='%Y%m%d')
overall_monthly['Рост продаж %'] = overall_monthly['Продажи'].pct_change() 
#----------------------------------------------------------------------------------------------------------------
point_monthly = sales_data.groupby(['точка', 'Год-мес']).agg({
    'Количество': 'sum',
    'Продажи': 'sum',
    'Себестоимость': 'sum',
    'Прибыль': 'sum',
    'Средняя цена': 'mean'
}).reset_index()
point_monthly['Год-мес'] = pd.to_datetime(point_monthly['Год-мес'] + '01', format='%Y%m%d')
point_monthly['Рост продаж %'] = point_monthly.groupby('точка')['Продажи'].pct_change() * 100
#----------------------------------------------------------------------------------------------------------------
avg_sales_per_point = sales_data.groupby('точка').agg({
    'Продажи': 'mean',
    'Количество': 'mean',
    'Себестоимость': 'mean',
    'Средняя цена': 'mean'
}).reset_index()
#----------------------------------------------------------------------------------------------------------------
model_monthly = sales_data.groupby(['модель', 'бренд', 'Год-мес']).agg({
    'Количество': 'sum',
    'Продажи': 'sum',
    'Себестоимость': 'sum',
    'Средняя цена': 'mean',
    'Прибыль': 'sum'
}).reset_index()
model_monthly['Год-мес'] = pd.to_datetime(model_monthly['Год-мес'] + '01', format='%Y%m%d')
model_monthly['Рост продаж %'] = model_monthly.groupby(['модель', 'бренд'])['Продажи'].pct_change() * 100
#----------------------------------------------------------------------------------------------------------------
unique_models = sales_data['модель'].unique()
unique_points = sales_data['точка'].unique()
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
BASE_DIR = 'summary'
os.makedirs('summary', exist_ok=True)
#----------------------------------------------------------------------------------------------------------------
os.makedirs(os.path.join(BASE_DIR, "overall"), exist_ok=True)

plt.figure(figsize=(12, 6))
sns.lineplot(data=overall_monthly, x='Год-мес', y='Продажи', marker='o')
plt.title('Динамика общего товарооборота (Продажи)')
plt.xlabel('Месяц')
plt.ylabel('Продажи')
plt.xticks(rotation=45)
plt.grid(True)
plt.savefig('summary/overall/overall_sales_dynamics.png')
plt.close()
#----------------------------------------------------------------------------------------------------------------
plt.figure(figsize=(12, 6))
sns.lineplot(data=overall_monthly, x='Год-мес', y='Количество', marker='o', label='Количество')
sns.lineplot(data=overall_monthly, x='Год-мес', y='Себестоимость', marker='o', label='Себестоимость')
sns.lineplot(data=overall_monthly, x='Год-мес', y='Прибыль', marker='o', label='Прибыль')
plt.title('Динамика количества, себестоимости и прибыли (общая)')
plt.xlabel('Месяц')
plt.ylabel('Значения')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.savefig('summary/overall/overall_qty_cost_profit_dynamics.png')
plt.close()
#----------------------------------------------------------------------------------------------------------------
plt.figure(figsize=(12, 6))
sns.lineplot(data=overall_monthly, x='Год-мес', y='Рост продаж %', marker='o')
plt.title('Динамика роста/спада продаж % (общая)')
plt.xlabel('Месяц')
plt.ylabel('Рост %')
plt.xticks(rotation=45)
plt.grid(True)
plt.savefig('summary/overall/overall_growth_dynamics.png')
plt.close()
#----------------------------------------------------------------------------------------------------------------
plt.figure(figsize=(12, 6))
sns.lineplot(data=overall_monthly, x='Год-мес', y='Средняя цена', marker='o')
plt.title('Динамика средней цены (общая)')
plt.xlabel('Месяц')
plt.ylabel('Средняя цена')
plt.xticks(rotation=45)
plt.grid(True)
plt.savefig('summary/overall/overall_avg_price_dynamics.png')
plt.close()
#----------------------------------------------------------------------------------------------------------------
plt.figure(figsize=(12, 6))
sns.barplot(data=avg_sales_per_point, x='точка', y='Продажи')
plt.title('Средние продажи по точкам')
plt.xlabel('Точка')
plt.ylabel('Средние продажи')
plt.xticks(rotation=45)
plt.grid(True)
plt.savefig('summary/overall/avg_sales_per_point.png')
plt.close()
#----------------------------------------------------------------------------------------------------------------
os.makedirs(os.path.join(BASE_DIR, "points"), exist_ok=True)

for point in unique_points:
    point_data = point_monthly[point_monthly['точка'] == point]
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=point_data, x='Год-мес', y='Продажи', marker='o')
    plt.title(f'Динамика продаж для точки: {point}')
    plt.xlabel('Месяц')
    plt.ylabel('Продажи')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.savefig(f'summary/points/sales_dynamics_point_{point.replace(" ", "_")}.png')
    plt.close()
#----------------------------------------------------------------------------------------------------------------
os.makedirs(os.path.join(BASE_DIR, "models_stat/sales_dynamics"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "models_stat/qty_dynamics"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "models_stat/cost_dynamics"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "models_stat/avg_price_dynamics"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "models_stat/growth_dynamics"), exist_ok=True)

# os.makedirs('models_stat/sales_dynamics', exist_ok=True)
# os.makedirs('models_stat/qty_dynamics', exist_ok=True)
# os.makedirs('models_stat/cost_dynamics', exist_ok=True)
# os.makedirs('models_stat/avg_price_dynamics', exist_ok=True)
# os.makedirs('models_stat/growth_dynamics', exist_ok=True)

for model in unique_models:
    model_data = model_monthly[model_monthly['модель'] == model]
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=model_data, x='Год-мес', y='Продажи', hue='бренд', marker='o')
    plt.title(f'Динамика продаж для модели: {model} (по брендам)')
    plt.xlabel('Месяц')
    plt.ylabel('Продажи')
    plt.legend(title='Бренд')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.savefig(f'summary/models_stat/sales_dynamics/sales_dynamics_model_{model}.png')
    plt.close()
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=model_data, x='Год-мес', y='Количество', hue='бренд', marker='o')
    plt.title(f'Динамика количества для модели: {model} (по брендам)')
    plt.xlabel('Месяц')
    plt.ylabel('Количество')
    plt.legend(title='Бренд')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.savefig(f'summary/models_stat/qty_dynamics/qty_dynamics_model_{model}.png')
    plt.close()
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=model_data, x='Год-мес', y='Себестоимость', hue='бренд', marker='o')
    plt.title(f'Динамика себестоимости для модели: {model} (по брендам)')
    plt.xlabel('Месяц')
    plt.ylabel('Себестоимость')
    plt.legend(title='Бренд')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.savefig(f'summary/models_stat/cost_dynamics/cost_dynamics_model_{model}.png')
    plt.close()
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=model_data, x='Год-мес', y='Средняя цена', hue='бренд', marker='o')
    plt.title(f'Динамика средней цены для модели: {model} (по брендам)')
    plt.xlabel('Месяц')
    plt.ylabel('Средняя цена')
    plt.legend(title='Бренд')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.savefig(f'summary/models_stat/avg_price_dynamics/avg_price_dynamics_model_{model}.png')
    plt.close()
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=model_data, x='Год-мес', y='Рост продаж %', hue='бренд', marker='o')
    plt.title(f'Динамика роста/спада продаж % для модели: {model} (по брендам)')
    plt.xlabel('Месяц')
    plt.ylabel('Рост %')
    plt.legend(title='Бренд')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.savefig(f'summary/models_stat/growth_dynamics/growth_dynamics_model_{model}.png')
    plt.close()
#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
# os.makedirs('forecast', exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "forecast"), exist_ok=True)
forecasts = {}
for model in unique_models:
    for brand in sales_data[sales_data['модель'] == model]['бренд'].unique():
        prod_data_ts = model_monthly[(model_monthly['модель'] == model) & (model_monthly['бренд'] == brand)].set_index('Год-мес')['Продажи']
        if len(prod_data_ts) >= 12:
            try:
                hw_model = ExponentialSmoothing(prod_data_ts, trend='add', seasonal='add', seasonal_periods=12)
                hw_fit = hw_model.fit()
                hw_forecast = hw_fit.forecast(12)
                forecasts[(model, brand)] = hw_forecast

                plt.figure(figsize=(12, 6))
                sns.lineplot(x=prod_data_ts.index, y=prod_data_ts.values, marker='o', label='Исторические продажи')
                sns.lineplot(x=hw_forecast.index, y=hw_forecast.values, marker='o', label='Прогноз')
                plt.title(f'Прогноз продаж для модели: {model}, бренд: {brand}')
                plt.xlabel('Месяц')
                plt.ylabel('Продажи')
                plt.legend()
                plt.xticks(rotation=45)
                plt.grid(True)
                plt.savefig(f'summary/forecast/forecast_model_{model}_brand_{brand.replace(" ", "_")}.png')
                plt.close()
            except:
                print(f'Не удалось построить прогноз для модели {model}, бренда {brand}')
#----------------------------------------------------------------------------------------------------------------
print('Анализ завершен. Графики сгруппированы по моделям и брендам. Файлы сохранены.')