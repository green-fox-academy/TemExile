import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt 
from function import get_bed, get_year, get_hold, get_home, new_build
import math
from sklearn.ensemble import GradientBoostingRegressor as gbr

df = pd.read_csv('newdata.csv', index_col=0)
x = df.drop('Price', axis = 1)
y = df['Price'].apply(math.log)
lower = 0.1
upper = 0.9
l_model = gbr(loss = 'quantile', alpha = lower)
u_model = gbr(loss = 'quantile', alpha = upper)
pre_model = gbr(loss = 'ls')
l_model.fit(x, y)
u_model.fit(x, y)
pre_model.fit(x, y)

math.exp(l_model.predict([[3,2,3,0,51.38945,-2.40103]]))
math.exp(u_model.predict([[3,2,3,0,51.38945,-2.40103]]))
math.exp(pre_model.predict([[3,2,3,0,51.38945,-2.40103]]))

pre_model.score(x, y)