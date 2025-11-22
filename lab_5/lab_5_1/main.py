from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

try:
    with open("countries.txt", 'r') as f:
        countries_list = f.read().split("\n")
except:
    raise ValueError("File error")

headers = {
    "User-Agent": "'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Mobile Safari/537.36'"
}
data = {
    "name": [],
    "capital": [],
    "area (km2)": [],
    "population": [],
}

for country in countries_list:
    if not country.strip(): 
        continue
    # ------------------------------------------------------------------------------------------------------
    url = f"https://en.wikipedia.org/wiki/{country}"
    # ------------------------------------------------------------------------------------------------------
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(f"Статус: {response.status_code}")
    except Exception as e:
        print(f"Ошибка при запросе для {country}: {e}")
        data["name"].append(country)
        data["capital"].append("")
        data["area (km2)"].append("")
        data["population"].append("")
        continue
    # ------------------------------------------------------------------------------------------------------    
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('h1').get_text().strip()
    print("Name:", title)
    data["name"].append(title)
    # ------------------------------------------------------------------------------------------------------
    capital_found = False
    area_found = False
    population_found = False
    capital = ""
    area = ""
    population = ""
    # ------------------------------------------------------------------------------------------------------
    infobox = soup.find('table', class_='infobox')
    for row in infobox.find_all('tr'):
        header = row.find('th')
        if not header:
            continue
        header_text = header.get_text().strip()
        # ------------------------------------------------------------------------------------------------------
        if not capital_found and 'Capital' in header_text:
                capital_link = row.find('td')
                if capital_link:
                    capital_a = capital_link.find('a')
                    if capital_a:
                        capital = capital_a.get_text().strip()
                    else:
                        capital = capital_link.get_text().strip().split('\n')[0]
                print("Capital:", capital)
                capital_found = True
        # ------------------------------------------------------------------------------------------------------        
        if not area_found and 'Area' in header_text:
                td = row.find('td')
                if not td:
                    next_row = row.find_next_sibling()
                    if next_row:
                        td = next_row.find("td")
                if td:
                    td_text = td.get_text()
                    numbers = re.findall(r'[\d,]+', td_text)
                    if numbers:
                        area = numbers[0].replace(',', '')
                        print("Area:", area)
                        area_found = True
        # ------------------------------------------------------------------------------------------------------
        if not population_found and 'Population' in header_text:
                td = row.find('td')
                if not td:
                    next_row = row.find_next_sibling()
                    if next_row:
                        td = next_row.find("td")
                if td:
                    text = td.get_text()
                    numbers = re.findall(r'[\d,]+', text)
                    if numbers:
                        population = numbers[0].replace(',', '')
                        print("Population:", population)
                        population_found = True
        # ------------------------------------------------------------------------------------------------------                
        if capital_found and area_found and population_found:
                break
    # --------------------------------------------------------------------------------------------------------            
    data['capital'].append(capital)
    data['area (km2)'].append(area)
    data['population'].append(population)

df = pd.DataFrame(data)
df.to_csv("countries.csv", index=0)