import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 
import math
from function import get_bed, get_hold, get_home, get_year, new_build

rawdf = pd.read_csv('Raw_data.csv', index_col=0)
rawdf = rawdf[rawdf['Bedroom'] != 'Unknown']
rawdf['Year'] = rawdf['SoldDate'].apply(get_year)
rawdf = rawdf[rawdf['Year'] >= '2015']
rawdf['Bedroom'] = rawdf['Bedroom'].apply(get_bed)
rawdf['New'] = rawdf['Type'].apply(new_build)
df = rawdf[['Bedroom', 'HoldType', 'HomeType', 'Price', 'New', 'areaCode', 'Year']]
df = df.rename(columns = {'areaCode':'postcode'})
ind = pd.Series([x for x in range(len(df))])
df = df.set_index(ind)
po = pd.read_csv('ukpostcodes.csv', index_col=0)
graph_df = df.merge(po, on = 'postcode')
# plt.hist(graph_df['Price'].apply(math.log))
# plt.xlabel('Price with Log-transfermation')
# plt.hist(graph_df['Price'])
# plt.xlabel('Price')
# plt.ylabel('Number of Obervations')
# box_df = graph_df[['Price', 'HomeType']]
# box_df['Price'] = box_df['Price'].apply(math.log)
# box_df.boxplot(by = 'HomeType')
# plt.xlabel('Home Type')
# hold_df = graph_df[['HoldType', 'Price']]
# hold_df['Price'] = hold_df['Price'].apply(math.log)
# hold_df.boxplot(by = 'HoldType')
# plt.xlabel('Hold Type')
# new_df = graph_df[['New', 'Price']]
# new_df['Price'] = new_df['Price'].apply(math.log)
# new_df.boxplot(by = 'New')
# plt.xlabel('New Building')
plt.scatter(x = sorted(graph_df['Bedroom']), y = graph_df['Price'].apply(math.log))
plt.xlabel('Number of Bedroom')
plt.title('')
plt.ylabel('Price on Log-transfermation')
plt.show()
