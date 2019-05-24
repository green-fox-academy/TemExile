from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/greeting')
def load_language():
    with open('language.txt', encoding = 'UTF-8', mode = 'r') as infile:
        greet = infile.readlines()
    x = random.randint(0,len(greet)-1)
    code = render_template('language.html', greeints = greet[x])
    return code

if __name__ == '__main__':
    app.run(debug=True)