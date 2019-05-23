from flask import Flask, jsonify, request, render_template, make_response
import json

app = Flask(__name__)

@app.route('/api/movies')
def api_get_all_movies():
    with open('movie.json') as infile:
        a = json.load(infile)
    respose = jsonify(a)
    return respose

@app.route('/api/<movie_id>')
def api_get_movie(movie_id):
    with open('movie.json') as infile:
        a = json.load(infile)
    for line in a:
        if movie_id == line['ID']:
            response = jsonify(line)
    return response

@app.route('/api/movie', methods = ['POST'])
def api_post_movie():
    api_key = '123'
    moviedic = jsonify(ID = '5', title = 'new movie', content = 'new content')
    # body = request.get_json()
    if request.headers['api_key'] == api_key:
        # with open('movie.json', 'r') as infile:
        #     a = json.load(infile)
        #     newid = str(len(a))
        # body["ID"] = newid
        # with open('movie.json', 'w') as finfile:
        #     a.append(body)
        #     json.dump(a, infile)
        response = jsonify(Result = 'Request completed')
        resp = make_response(response, 200)
        return resp
    else:
        response = jsonify(error = 'Invalid API_KEY')
        resp = make_response(response, 403)
        return resp

@app.route('/api/put/<movie_id>', methods = ['PUT'])
def api_put_movie(movie_id):
    api_key = '123'
    # body = request.get_json()
    # moviedic = {"ID" = movie_id, "title" = 'new movie', "content" = 'new content'}
    if request.headers['api_key'] == api_key:
        with open('movie.json', 'r') as infile:
            a = json.load(infile)
        response = jsonify(error = f'No movie found wiht {movie_id} ID')
        resp = make_response(response, 404)
        for l in a:
            if movie_id == l["ID"]:
                #l["title"] = moviedic["title"]
                #l["content"] = moviedic["content"]
                # with open('movie.json', 'w') as infile:
                #     json.dumps(a, infile)
                response = jsonify(Result = "Request completed")
                resp = make_response(response, 200)
            else:
                pass
        return resp
    else:
        response = jsonify(error = 'Invalid API_KEY')
        resp = make_response(response, 403)
        return resp

@app.route('/api/delete/<movie_id>', methods = ['DELETE'])
def api_delete(movie_id):
    api_key = '123'
    if request.headers['api_key'] == api_key:
        with open('movie.json', 'r') as infile:
            a = json.load(infile)
        response = jsonify(error = f'No movie found wiht {movie_id} ID')
        resp = make_response(response, 404)
        for l in a:
            if movie_id == l["ID"]:
                # a.remove(l)
                # with open('movie.json', 'w') as infile:
                #     json.dumps(a, infile)
                response = jsonify(Result = "Request completed")
                resp = make_response(response, 200)
            else:
                pass
        return resp
    else:
        response = jsonify(error = 'Invalid API_KEY')
        resp = make_response(response, 403)
        return resp

        


if __name__ == '__main__':
    app.run(debug=True)
