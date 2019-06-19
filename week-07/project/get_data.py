import requests
from bs4 import BeautifulSoup
import numpy as np 
import pandas as pd 
from function import get_info

city_list = {
    'Bath':'116', 'Bridgwater':'212', 'Burnham-On-Sea':'251', 'Chard':'301', 
    'Cheddar':'306', 'Clevedon':'337', 'Crewkerne':'381',
    'Frome':'536', 'Glastonbury':'551', 'Ilminster':'678', 'Minehead':'942', 
    'Radstock':'1109', 'Shepton+Mallet':'1198',
    'Street':'1287', 'Taunton':'1317', 'Wellington':'1414', 'Wells':'1415', 
    'Weston-Super-Mare':'1437', 'Wincanton':'1458', 'Yeovil':'1497'
}
# 'https://www.rightmove.co.uk/house-prices/detail.html?'
# 'country=england&locationIdentifier=REGION%5E1198&'
# 'searchLocation=Shepton+Mallet&referrer=listChangeCriteria&index=0'
page_list = [x*25 for x in range(40)]
base_url = r'https://www.rightmove.co.uk/house-prices/detail.html?country=england&locationIdentifier=REGION%5E'

raw_data_list = []
for key, value in city_list.items():
    for n in page_list:
        url = base_url + value + r'&searchLocation=' + key + '&&referrer=listChangeCriteria&index=' + str(n)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        data = soup.find_all('li', 'soldUnit')
        for item in data:
            dic = {}
            result = get_info(item)
            dic['Price'] = result[0]
            dic['HomeType'] = result[1]
            dic['HoldType'] = result[2]
            dic['Type'] = result[3]
            dic['SoldDate'] = result[4]
            dic['Bedroom'] = result[5]
            dic['areaCode'] = result[6]
            dic['City'] = key
            raw_data_list.append(dic)
      
df = pd.DataFrame(raw_data_list)
df.to_csv('Raw_data.csv')