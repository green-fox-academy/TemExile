from flask import Flask, render_template, request, redirect, make_response
import json


app = Flask(__name__)

@app.route('/')
def log_page():
    return redirect('login')

@app.route('/login')
def log_in():
    return render_template('login.html')

@app.route('/sign-up')
def sign_up():
    return render_template("signup.html")

@app.route('/api/login', methods = ["POST"])
def check_info():
    username = request.form['username']
    password = request.form['password']
    info = {"username":username, "password":password}
    with open('info.json', 'r') as infile:
        a = json.load(infile)
    for i in a:
        if i['username'] == info['username'] and i['password'] == info['password']:
            return render_template("welcome.html", username = username)
    return make_response('Invalid username or password', 403)

@app.route('/api/sign-up', methods = ["POST"])
def sign():
    username = request.form['username']
    password = request.form['password']
    cpassword = request.form['password']
    newinfo = {"username":username, "password":password}
    with open('info.json', 'r') as infile:
        a = json.load(infile)
    if password != cpassword:
        return make_response('Please enter the same password', 403)
    else:
        for dic in a:
            if dic['username'] == newinfo['username']:
                return make_response("username exited", 403)
        a.append(newinfo)
        with open('info.json', 'w') as infile:
            json.dump(a, infile)
        return render_template('welcome.html', username = username)

if __name__ == '__main__':
    app.run(debug=True)