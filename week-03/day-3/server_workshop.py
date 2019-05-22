from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/exercise1')
def show_exercise1(name = None):
    return render_template('exercise1.html', name = name)

@app.route('/exercise2')
def show_exercise2(name = None):
    return render_template('exercise2.html', name = name)

@app.route('/exercise3')
def show_exercise3(name = None):
    return render_template('exercise3.html', name = name)

@app.route('/exercise4')
def show_exercise4(name = None):
    return render_template('exercise4.html', name = name)

@app.route('/exercise5')
def show_exercise5(name = None):
    return render_template('exercise5.html', name = name)

@app.route('/')
def show_exercise(name = None):
    return render_template('first_web.html', name = name)


if __name__=='__main__':
    app.run(debug=True)