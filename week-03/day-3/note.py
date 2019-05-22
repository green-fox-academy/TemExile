from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/<name>')
def hello_name(name):
    return f'hello {name}'

if __name__ == '__main__':
    app.run(debug=True)
'''
@app.route('/cat')
def cat():
    return 'cat'
'''

'''
from flask import request
@app.route('/cat')
def cat():
    return f"how are you {request.args.get('name', 'anonymus')})?"

@app.route('<useruse>')
def hello_name(username):
    return render_template('index.html', name = username)
'''