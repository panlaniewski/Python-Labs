from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import time
import argparse
import os
from urllib.parse import quote
# -----------------------------------------------------------------------------------------------------------
def setup_args():
    parser = argparse.ArgumentParser(description='Парсер стран из Википедии')
    parser.add_argument('-i', '--input', default='countries.txt', 
                       help='Имя входного файла со списком стран (по умолчанию: countries.txt)')
    parser.add_argument('-o', '--output', default='countries_data.csv', 
                       help='Имя выходного CSV файла (по умолчанию: countries_data.csv)')
    parser.add_argument('-c', '--cache', default='cache', 
                       help='Папка для кэша страниц (по умолчанию: cache)')
    parser.add_argument('-d', '--delay', type=float, default=1.0,
                       help='Задержка между запросами в секундах (по умолчанию: 1.0)')
    return parser.parse_args()
# -----------------------------------------------------------------------------------------------------------
def ensure_cache_dir(cache_dir):
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
        print(f"Создана папка кэша: {cache_dir}")
# -----------------------------------------------------------------------------------------------------------
def get_cached_page(country, cache_dir, headers):
    # Создаем безопасное имя файла для кэша
    safe_country = quote(country, safe='')
    cache_file = os.path.join(cache_dir, f"{safe_country}.html")
    # -----------------------------------------------------------------------------------------------------------
    # Если файл существует в кэше, читаем его
    if os.path.exists(cache_file):
        print(f"Чтение из кэша: {country}")
        with open(cache_file, 'r', encoding='utf-8') as f:
            return f.read()
    # -----------------------------------------------------------------------------------------------------------
    # Если нет в кэше, загружаем
    url = f"https://en.wikipedia.org/wiki/{country}"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        # -----------------------------------------------------------------------------------------------------------
        # Сохраняем в кэш
        with open(cache_file, 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"Страница загружена и сохранена в кэш: {country}")
        
        return response.text
    except Exception as e:
        print(f"Ошибка при загрузке страницы {country}: {e}")
        return None
# -----------------------------------------------------------------------------------------------------------
def parse_country_info(soup, country_name):
    capital = ""
    area = ""
    population = ""
    # -----------------------------------------------------------------------------------------------------------
    infobox = soup.find('table', class_='infobox')
    if not infobox:
        print(f"Инфобокс не найден для {country_name}")
        return capital, area, population
    # -----------------------------------------------------------------------------------------------------------
    # Ищем все строки с заголовками
    rows = infobox.find_all('tr')
    for row in rows:
        th = row.find('th')
        if th:
            th_text = th.get_text().strip().lower()
            # Проверяем различные варианты написания
            if any(word in th_text for word in ['capital', 'capitals', 'capital city']):
                td = row.find('td')
                if td:
                    # Ищем первую ссылку в ячейке - обычно это столица
                    capital_link = td.find('a')
                    if capital_link:
                        capital = capital_link.get_text().strip()
                        break
                    else:
                        # Если нет ссылки, берем чистый текст
                        capital_text = td.get_text().strip()
                        capital = capital_text.split('\n')[0].split('[')[0].split('(')[0].strip()
                        if capital:
                            break
    # -----------------------------------------------------------------------------------------------------------
    # Поиск площади
    for row in rows:
        th = row.find('th')
        if th and 'area' in th.get_text().lower():
            td = row.find('td')
            if not td:
                next_row = row.find_next_sibling('tr')
                if next_row:
                    td = next_row.find('td')
            if td:
                area_text = td.get_text()
                numbers = re.findall(r'[\d,]+', area_text)
                if numbers:
                    area = numbers[0].replace(',', '')
            break
    # -----------------------------------------------------------------------------------------------------------
    # Поиск населения
    for row in rows:
        th = row.find('th')
        if th and 'population' in th.get_text().lower():
            td = row.find('td')
            if not td:
                next_row = row.find_next_sibling('tr')
                if next_row:
                    td = next_row.find('td')
            if td:
                population_text = td.get_text()
                numbers = re.findall(r'\d{1,3}(?:,\d{3})*', population_text)
                if numbers:
                    clean_numbers = [num.replace(',', '') for num in numbers]
                    population = max(clean_numbers, key=len)
            break 
    print(f"Столица: {capital if capital else 'не найдена'}")
    return capital, area, population
# -----------------------------------------------------------------------------------------------------------
def main():
    # Получаем аргументы командной строки
    args = setup_args()
    # Создаем папку для кэша
    ensure_cache_dir(args.cache)
    # Загружаем список стран
    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            countries_list = [c.strip() for c in f.read().split("\n") if c.strip()]
        print(f"Загружено {len(countries_list)} стран из файла {args.input}")
    except FileNotFoundError:
        print(f"Ошибка: файл {args.input} не найден!")
        return
    except Exception as e:
        print(f"Ошибка при чтении файла {args.input}: {e}")
        return
    # -----------------------------------------------------------------------------------------------------------
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    data = {
        "country": [],
        "city": [],
        "area": [],
        "population": []
    }
    # -----------------------------------------------------------------------------------------------------------
    for i, country in enumerate(countries_list, 1):
        print(f"\n[{i}/{len(countries_list)}] Обработка: {country}")
        # Получаем страницу (из кэша или интернета)
        html_content = get_cached_page(country, args.cache, headers)
        if html_content is None:
            # Если страница не загрузилась, добавляем пустые данные
            data["country"].append(country)
            data["city"].append("")
            data["area"].append("")
            data["population"].append("")
            continue
        soup = BeautifulSoup(html_content, 'html.parser')
        # Получаем официальное название страны из заголовка
        country_name = soup.find('h1').get_text().strip()
        print(f"Country: {country_name}")
        # -----------------------------------------------------------------------------------------------------------
        # Парсим информацию о стране
        capital, area, population = parse_country_info(soup, country_name)
        data["country"].append(country_name)
        data["city"].append(capital)
        data["area"].append(area)
        data["population"].append(population)
        # Пауза между запросами (кроме последней итерации)
        if i < len(countries_list):
            print(f"Пауза {args.delay} секунд...")
            time.sleep(args.delay)
    # -----------------------------------------------------------------------------------------------------------
    # Сохраняем результаты в CSV
    df = pd.DataFrame(data)
    df.to_csv(args.output, index=False)

if __name__ == "__main__":
    main()