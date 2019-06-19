import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt 
from function import get_bed, get_year, get_hold, get_home, new_build
import math

rawdf = pd.read_csv('Raw_data.csv', index_col = 0)
rawdf = rawdf[rawdf['Bedroom'] != 'Unknown']
rawdf['Year'] = rawdf['SoldDate'].apply(get_year)
rawdf['Bedroom'] = rawdf['Bedroom'].apply(get_bed)
rawdf = rawdf[rawdf['Year'] >= '2015']
rawdf['NewBuilding'] = rawdf['Type'].apply(new_build)
rawdf['HoldType'] = rawdf['HoldType'].apply(get_hold)
rawdf['HomeType'] = rawdf['HomeType'].apply(get_home)

model_df = rawdf[['Bedroom', 'HoldType', 'HomeType', 'Price', 'areaCode', 'NewBuilding']]
lat_long_df = pd.read_csv('ukpostcodes.csv', index_col = 0)
model_df = model_df.rename(columns = {'areaCode':'postcode'})
model_df = model_df.merge(lat_long_df, on = 'postcode')
model_df = model_df.drop('postcode', axis = 1)
model_df.to_csv('newdata.csv')

x_value = model_df.drop('Price', axis = 1)
y_value = model_df['Price'].apply(math.log)
lm = LinearRegression()
lm.fit(x_value, y_value)
y_pred = lm.predict(x_value)
lm.score(x_value, y_value)
