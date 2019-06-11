from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
from pandas.io.json import json_normalize
from nameandprice import get_name, get_price

page = requests.get('https://www.alza.co.uk/basic-home-and-office-laptops/18843464.htm')
soup = BeautifulSoup(page.content, 'html.parser')
home_and_office_top3_info = soup.find_all('div', class_= 'firstRow')
home_and_office = {}
for item in home_and_office_top3_info:
    name = get_name(item)
    price = get_price(item)
    home_and_office[name] = price

page = requests.get('https://www.alza.co.uk/gaming-laptops/18848814.htm')
soup = BeautifulSoup(page.content, 'html.parser')
gaming_top3_info = soup.find_all('div', class_= 'firstRow')
gaming = {}
for item in gaming_top3_info:
    name = get_name(item)
    price = get_price(item)
    gaming[name] = price

page = requests.get('https://www.alza.co.uk/professional-laptops/18853299.htm')
soup = BeautifulSoup(page.content, 'html.parser')
professional_top3_info = soup.find_all('div', class_= 'firstRow')
professional = {}
for item in professional_top3_info:
    name = get_name(item)
    price = get_price(item)
    professional[name] = price

print(home_and_office)
print(gaming)
print(professional)