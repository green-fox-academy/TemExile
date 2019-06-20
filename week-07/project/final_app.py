from flask import Flask, request, render_template
from function import get_bed, get_year, get_loc, gbr_model, new_function, get_hold, get_home
import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression
import math

app = Flask(__name__)
@app.route('/')
def first_page():
    return render_template('first_page.html')

@app.route('/quote', methods = ['POST'])
def quote_page():
    Bedroom = request.form['Bedroom']
    HoldType = request.form['HoldType']
    HomeType = request.form['HomeType']
    NewBuilding = request.form['NewBuilding']
    postcode = request.form['postcode']
    lat, long = get_loc(postcode)
    Hold = get_hold(HoldType)
    Home = get_home(HomeType)
    New = new_function(NewBuilding)
    input_x = [[int(Bedroom), Hold, Home, New, lat, long]]
    lower_model, upper_model, pred = gbr_model()
    y_pred = pred.predict(input_x)
    price = round(math.exp(y_pred),2)
    l_bound = round(math.exp(lower_model.predict(input_x)),2)
    u_bound = round(math.exp(upper_model.predict(input_x)),2)
    return render_template('quote.html', price = price, lower = l_bound, upper = u_bound)


if __name__=='__main__':
    app.run(debug=True)