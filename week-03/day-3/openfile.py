from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route('/first_page')
def first_page():
    return render_template('first_page.html')

@app.route('/')
def redirect_page():
    return redirect('first_page')

@app.route('/first_page/<movie_id>')
def movie_name(movie_id):
    with open('movie.json', 'r') as infile:
        moviedir = json.load(infile)
    movie_list = []
    for line in moviedir:
        movie_list.append(line)
    choose = int(movie_id) - 1
    choose_movie = movie_list[choose]
    return render_template('movie.html', 
    title = choose_movie['title'], header = choose_movie['title'], 
    body = choose_movie['content'])


if __name__ == '__main__':
    app.run(debug=True)