from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
from pandas.io.json import json_normalize
from dtnamenameprice import get_dtname, get_dtprice

page = requests.get('https://www.pbtech.com/category/computers/pcs/shop-all')
soup = BeautifulSoup(page.content, 'html.parser')
name = soup.find_all('div', class_ = 'item_description')
price = soup.find_all('div', class_ = 'item_buy')
first10name = name[:10]
first10price = price[:10]
desktop = {}
for i in range(len(first10name)):
    name = get_dtname(first10name[i])
    price = get_dtprice(first10price[i])
    desktop[name] = price

