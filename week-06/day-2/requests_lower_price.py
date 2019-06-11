import requests
import json
import pandas as pd
from pandas.io.json import json_normalize

url = 'https://api.skypicker.com/flights?flyFrom=BRS&to=PRG&dateFrom=18/12/2019&dateTo=23/12/2019&partner=picky&max_stopovers=0'
data = requests.get(url)
df = json.loads(data.text)
rawdata = df['data']
price_list = []
for i in rawdata:
    # print(i['price'])
    price_list.append(i['price'])
# print(min(price_list))
lowest_price_flight = rawdata[price_list.index(min(price_list))]