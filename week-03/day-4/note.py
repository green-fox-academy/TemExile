from flask import Flask, request, render_template, jsonify, make_response

app = Flask(__name__)

@app.route('/api')
def api_root():
    respose = jsonify(a = 12)
    return respose

@app.route('/api404')
def api_root_not():
    respose = make_response('not found', 404)
    return respose

@app.route('/apipost', methods = ['POST'])
def api_post():
    respose = jsonify(apple = 34, key = request.headers['x-api-key'])
    return respose
    
if __name__ == '__main__':
    app.run(debug=True)