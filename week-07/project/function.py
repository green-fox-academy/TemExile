import pandas as pd 
import numpy as np 
import math
from sklearn.linear_model import LinearRegression

def get_info(item):
    a = list(item)
    b = list(a[1])
    if len(b) == 5:
        c = list(b[3])
    elif len(b) == 4:
        c = list(b[2])
    d = list(c[1])
    price = float(list(d[1])[0][1:].replace(',', ''))
    HomeType = list(d[3])[0].split(',')[0]
    HoldType = list(d[3])[0].split(',')[1].lstrip()
    Usage = list(d[3])[0].split(',')[2].lstrip()
    SoldDate = list(d[5])[0]
    if len(list(d[7])) == 0:
        Bedroom = 'Unknown'
    elif len(list(d[7])) == 1:
        Bedroom = list(d[7])[0]
    areacode1 = list(b[1])[0].split(' ')[-2]
    areacode2 = list(b[1])[0].split(' ')[-1]
    areacode = areacode1 + ' ' + areacode2
    return [price, HomeType, HoldType, Usage, SoldDate, Bedroom, areacode]

def get_bed(value):
    return value.split()[0]
def get_year(value):
    return value[-4:]

def get_hold(value):
    if value == 'Freehold':
        return 2
    else:
        return 1

def get_home(value):
    if value == 'Semi-Detached':
        return 3
    elif value == 'Terraced':
        return 2
    elif value == 'Flat':
        return 1
    elif value == 'Detached':
        return 4

def new_build(value):
    new_building_len = 12
    if len(value) == new_building_len:
        return 1
    else:
        return 0

def new_function(value):
    if value == 'Yes':
        return 1
    else:
        return 0

def fit_model():
    df = pd.read_csv('newdata.csv', index_col = 0)
    x_value = df.drop('Price', axis = 1)
    y_value = df['Price'].apply(math.log)
    lm = LinearRegression()
    lm.fit(x_value, y_value)
    return lm

def get_loc(postcode):
    df = pd.read_csv('ukpostcodes.csv', index_col = 0)
    lat = float(df.loc[df['postcode'] == postcode, 'latitude'])
    long = float(df.loc[df['postcode'] == postcode, 'longitude'])
    return lat, long

