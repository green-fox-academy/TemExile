from flask import Flask, render_template, request, jsonify, make_response, redirect
import json

app = Flask(__name__)

@app.route('/movie')
def first_page():
    with open('gui.json', 'r') as infile:
        a = json.load(infile)
    return render_template('first_page.html', movielist = a)

@app.route('/')
def redi():
    return redirect('movie')

@app.route('/add-movie')
def add_movie():
    return render_template('add.html')

@app.route('/edit/<movie_id>')
def edit(movie_id):
    return render_template('edit.html', movie_id = movie_id)

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

@app.route('/api/movies/<movie_id>', methods = ['POST'])
def change(movie_id):
    ids = movie_id
    title = request.form['title']
    year = request.form['year']
    genre = request.form['genre']
    des = request.form['description']
    code = request.form['code']
    newmovie = {'id':ids, 'title':title, 'year':year, 'genre':genre, 'description':des}
    enterCode = '123'
    if code == enterCode:
        with open('gui.json', 'r') as infile:
            a = json.load(infile)
        response = jsonify(error = f'No movie found wiht {movie_id} ID')
        resp = make_response(response, 404)
        for l in a:
            if newmovie['id'] == l["id"]:
                x = a.index(l)
                a.pop(x)
                a.insert(x, newmovie)
                with open('gui.json', 'w') as infile:
                    json.dump(a, infile)
                response = jsonify(Result = "Request completed")
                resp = make_response(response, 200)
        return resp
    else:
        response = jsonify(error = 'Invalid Access Code')
        resp = make_response(response, 403)
        return resp



if __name__ == '__main__':
    app.run(debug=True)
