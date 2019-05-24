from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_table():
    products = [
    ("Milk", 3.59123),
    ("Bread", 2.96332),
    ("Rice", 0.64111)]
    return render_template('product.html', product = products)

if __name__=='__main__':
    app.run(debug=True)
    