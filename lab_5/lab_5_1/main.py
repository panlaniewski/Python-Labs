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
    url = f"https://en.wikipedia.org/wiki/{country}"

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print(f"Статус: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('h1').get_text().strip()
    print(title)
    data["name"].append(title)

    tables = soup.find_all("tr")
    capital = ""
    for row in tables:
        th = row.find('th')
        if th:
            if 'Capital' in th.get_text():
                td = row.find('td').find("a")
                if td:
                    capital = td.get_text()
                    break
    data["capital"].append(capital)

    mergedrows = soup.find_all("tr", class_="mergedrow")
    area = ""
    for row in mergedrows:
        th = row.find('th')
        if th:
            if 'Total' in th.get_text():
                td = row.find('td')
                if td:
                    area = td.get_text()
                    break
    area = area.split(" ")[0][:-4].replace(",", "")
    area = re.sub(r'\[.*?\]', '', area)
    data["area (km2)"].append(area)

    mergedtoprows = soup.find_all("tr", class_="mergedtoprow")
    population = ""
    for row in mergedtoprows:
        th = row.find('th')
        if th and th.find("a"):
            if 'Population' in th.find("a").get_text():
                tr = row.find_next('tr', class_='mergedrow')
                if tr:
                    text_nodes = tr.find("td").find_all(string=True, recursive=False)
                    if len(text_nodes) > 0:
                        population = text_nodes[0].strip()
                    else:
                        population = tr.find("td").get_text()
                    break
    population = population.replace(",", "")
    population = re.sub(r'\[.*?\]', '', population)
    data["population"].append(population)
    
df = pd.DataFrame(data)
df.to_csv("countries.csv", index=0)