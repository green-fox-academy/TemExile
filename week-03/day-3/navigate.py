from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/index')
def movie_index():
    return render_template('index.html')

@app.route('/')
def index():
    return redirect(url_for('movie_index'))

@app.route('/index/movie_id_1')
def movie_id_1():
    return render_template('theGodfather.html')

@app.route('/index/movie_id_2')
def movie_id_2():
    return render_template('theStarWar.html')

@app.route('/index/movie_id_3')
def movie_id_3():
    return render_template('theDarkKnight.html')

@app.route('/index/movie_id_4')
def movie_id_4():
    return render_template('theShawshank.html')

@app.route('/index/movie_id_5')
def movie_id_5():
    return render_template('PulpFiction.html')

if __name__ == '__main__':
    app.run(debug=True)