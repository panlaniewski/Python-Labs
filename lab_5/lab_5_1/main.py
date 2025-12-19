from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import time
import argparse
import json
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
    #python main.py -i countries.txt -o countries_data.csv -d 2.0
# -----------------------------------------------------------------------------------------------------------
# Функция получения данных из кэша
def get_cached_page(country_name):
    try:
        with open("cached_countries.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get(country_name)
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    except Exception as e:
        print(f"Ошибка при чтении кэша: {e}")
        return None
# -----------------------------------------------------------------------------------------------------------
# Функция сохранения в кэш
def save_to_cache(country_name, capital, area, population):
    try:
        try:
            with open("cached_countries.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
        # -----------------------------------------------------------------------------------------------------------
        data[country_name] = {
            "capital": capital,
            "area": area,
            "population": population,
        }
        # -----------------------------------------------------------------------------------------------------------
        with open("cached_countries.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        # -----------------------------------------------------------------------------------------------------------    
        print(f"Данные по {country_name} сохранены в кэш")
    # -----------------------------------------------------------------------------------------------------------    
    except Exception as e:
        print(f"Ошибка при сохранении в кэш: {e}")
# -------------------------------------------------------------------------------------------------------------------
# Функция загрузки страницы с сайта
def fetch_page(country_name):
    try:
        # Формируем URL для Википедии
        wiki_name = country_name.replace(' ', '_')
        url = f"https://en.wikipedia.org/wiki/{wiki_name}"
        # -----------------------------------------------------------------------------------------------------------
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        # -----------------------------------------------------------------------------------------------------------
        print(f"Загружаем страницу: {url}")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        # -----------------------------------------------------------------------------------------------------------
        return response.text
    # ---------------------------------------------------------------------------------------------------------------   
    except requests.RequestException as e:
        print(f"Ошибка при загрузке страницы {country_name}: {e}")
        return None
# -------------------------------------------------------------------------------------------------------------------
# Функция парсинга - сбора нужных для нас данных
def parse_country_info(soup, country_name):
    capital = ""
    area = ""
    population = ""
    # ---------------------------------------------------------------------------------------------------------------
    # Ищем HTML-элементы с искомыми данными
    infobox = soup.find('table', class_='infobox')
    # ---------------------------------------------------------------------------------------------------------------
    # Если не находим, то возвращаем пустые значения
    if not infobox:
        print(f"Инфобокс не найден для {country_name}")
        return capital, area, population
    # ---------------------------------------------------------------------------------------------------------------
    # Ищем все строки с заголовками
    rows = infobox.find_all('tr')
    # ---------------------------------------------------------------------------------------------------------------
    # Поиск столицы
    for row in rows:
        th = row.find('th')
        if th:
            th_text = th.get_text().strip().lower()
            # Проверяем различные варианты написания
            if any(word in th_text for word in ['capital', 'capitals', 'capital city']):
                td = row.find('td')
                if td:
                    # Ищем первую ссылку в ячейке, где может хранится строка столицы
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
    # ---------------------------------------------------------------------------------------------------------------
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
                # Форматируем строку, чтобы убрать ненужные символы
                numbers = re.findall(r'[\d,]+', area_text)
                if numbers:
                    area = numbers[0].replace(',', '')
            break
    # ---------------------------------------------------------------------------------------------------------------
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
                # Приводим значение численности населения к общему виду
                numbers = re.findall(r'\d{1,3}(?:,\d{3})*', population_text)
                if numbers:
                    clean_numbers = [num.replace(',', '') for num in numbers]
                    population = max(clean_numbers, key=len)
            break
    # ---------------------------------------------------------------------------------------------------------------
    return capital, area, population
# -----------------------------------------------------------------------------------------------------------
def main():
    # Получаем аргументы командной строки
    args = setup_args()
    # ---------------------------------------------------------------------------------------------------------------
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
    # ---------------------------------------------------------------------------------------------------------------
    # Подготавливаем структуру для данных
    data = {
        "country": [],
        "capital": [],  # Изменено с "city" на "capital" для согласованности
        "area": [],
        "population": []
    }
    # ---------------------------------------------------------------------------------------------------------------
    # Обрабатываем каждую страну
    for country in countries_list:
        print(f"\nОбработка: {country}")
        
        # Шаг 1: Проверяем кэш
        cached_data = get_cached_page(country)
        if cached_data:
            print(f"  Данные найдены в кэше")
            capital = cached_data.get("capital", "")
            area = cached_data.get("area", "")
            population = cached_data.get("population", "")
        else:
            # Шаг 2: Если нет в кэше, загружаем и парсим
            print(f"  Загружаем с сайта...")
            html_content = fetch_page(country)
            
            if html_content is None:
                print(f"  Не удалось загрузить данные")
                capital, area, population = "", "", ""
            else:
                soup = BeautifulSoup(html_content, 'html.parser')
                # ---------------------------------------------------------------------------------------------------------------
                # Получаем официальное название из заголовка
                country_name_elem = soup.find('h1')
                actual_country_name = country_name_elem.get_text().strip() if country_name_elem else country
                print(f"  Официальное название: {actual_country_name}")
                # ---------------------------------------------------------------------------------------------------------------
                # Парсим информацию
                capital, area, population = parse_country_info(soup, actual_country_name)
                # ---------------------------------------------------------------------------------------------------------------
                # Сохраняем в кэш
                if capital or area or population:
                    save_to_cache(actual_country_name, capital, area, population)
                else:
                    print(f"  Не удалось извлечь данные")
        # ---------------------------------------------------------------------------------------------------------------
        # Добавляем данные
        data["country"].append(country)
        data["capital"].append(capital)
        data["area"].append(area)
        data["population"].append(population)
        # ---------------------------------------------------------------------------------------------------------------
        # Пауза между запросами
        if args.delay > 0:
            time.sleep(args.delay)
    # -------------------------------------------------------------------------------------------------------------------
    # Сохраняем результаты в CSV
    df = pd.DataFrame(data)
    df.to_csv(args.output, index=False, encoding='utf-8')