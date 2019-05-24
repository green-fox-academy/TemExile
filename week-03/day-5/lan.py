from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/greeting_2')
def load_language():
    with open('lan.txt', encoding = 'UTF-8', mode = 'r') as infile:
        greet = infile.readlines()
    x = random.randint(0,len(greet)-1)
    with open('name.txt', encoding = 'UTF-8', mode = 'r') as infile:
        name = infile.readlines()
    y = random.randint(0, len(name)-1)
    code = render_template('lang.html', greeting = greet[x], name = name[y])
    return code

if __name__ == '__main__':
    app.run(debug=True)