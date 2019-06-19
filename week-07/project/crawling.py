import requests
from bs4 import BeautifulSoup

url = r'https://www.rightmove.co.uk/house-prices/Shepton-Mallet.html?country=england&locationIdentifier=REGION%5E1198&searchLocation=Shepton+Mallet&index=25'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
data = soup.find_all('li', 'soldUnit')

a = list(data[0])
b = list(a[1])
c = list(b[3])
d = list(c[1])
price = float(list(d[1])[0][1:].replace(',', ''))
HomeType = list(d[3])[0].split(',')[0]
HoldType = list(d[3])[0].split(',')[1]
Usage = list(d[3])[0].split(',')[2]
SoldDate = list(d[5])[0]
Bedroom = list(d[7])
postcode = list(b[1])[0][-7:]

a = list(data[1])
b = list(a[1])
c = list(b[2])
d = list(c[1])
price = float(list(d[1])[0][1:].replace(',', ''))
HomeType = list(d[3])[0].split(',')[0]
HoldType = list(d[3])[0].split(',')[1]
Usage = list(d[3])[0].split(',')[2]
SoldDate = list(d[5])[0]
Bedroom = list(d[7])
postcode = list(b[1])[0][-7:]