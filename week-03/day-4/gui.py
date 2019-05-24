from flask import Flask, render_template, request, jsonify, make_response, redirect
import json

app = Flask(__name__)

@app.route('/movie')
def first_page():
    return render_template('first_page.html')

@app.route('/')
def redi():
    return redirect('movie')

@app.route('/add-movie')
def add_movie():
    return render_template('add.html')

@app.route('/api/movies', methods = ['POST'])
def get_data():
    title = request.form['title']
    year = request.form['year']
    genre = request.form['genre']
    des = request.form['description']
    code = request.form['code']
    newmovie = {'title':title, 'year':year, 'genre':genre, 'description':des}
    enterCode = '123'
    if code == enterCode:
        with open('gui.json', 'r') as infile:
            a = json.load(infile)
            newid = str(len(a) + 1)
        newmovie['id'] = newid
        with open('gui.json', 'w') as infile:
            a.append(newmovie)
            json.dump(a, infile)
        response = jsonify(Result = 'Request completed')
        resp = make_response(response, 200)
        return resp
    else:
        response = jsonify(error = 'Invalid Access Code')
        resp = make_response(response, 403)
        return resp

# @app.route('/api/movies/<movie_id>')


if __name__ == '__main__':
    app.run(debug=True)
