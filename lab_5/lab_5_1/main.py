from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Belarus'
headers = {
    "User-Agent": "'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Mobile Safari/537.36'"
}
response = requests.get(url, headers=headers)
response.raise_for_status()
print(f"Статус: {response.status_code}")
print(response.text)