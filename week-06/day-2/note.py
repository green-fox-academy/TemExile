import requests
import json
import pandas as pd
from pandas.io.json import json_normalize
from bs4 import BeautifulSoup

BaseUrl = 'https://api.skypicker.com/airlines'
GettingData = requests.get(BaseUrl)

Df = json.loads(GettingData.text)

Df1 = json_normalize(Df)

Df1["lcc"] = pd.to_numeric(Df1["lcc"])

Df2 = Df1[Df1['lcc'] != 'None']

Df2["lcc"] = pd.to_numeric(Df2["lcc"])

Df2.info()

Df2[Df2['lcc'] == 1].count()

Df2.head()
Df2.describe(include = 'all')


page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

page.content
soup = BeautifulSoup(page.content)
print(soup.prettify())
html = list(soup.children)[2]
body = list(html.children)[3]
list(body.children)
p = list(body.children)[1]
list(p.children)
p.get_text()

soup.find_all('p')
soup.find_all('title')

page = requests.get("https://blog.hartleybrody.com/web-scraping/")

soup = BeautifulSoup(page.content, 'html.parser')

soup.find_all('div', class_='post-callout')