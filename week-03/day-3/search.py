from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/search')
def search():
    b = request.args
    print(b)
    b.get('name')
    with open('products.csv', 'r') as infile:
        a = infile.readlines()
    plist = []
    a = a[1:]
    for line in a:
        line = line[:-1]
        xx = line.split(';')
        plist.append(xx)
    for l in plist:
        if b.get('name') in l:
            result = 'ID: '+l[0]+'Name: '+l[1]+'Price: '+l[2]+'Quantity: '+l[3]
            break
        elif b.get('name', '') == '':
            result = ''
        else:
            result = 'We do not have the Product' 
    return render_template('search.html', result = result)


@app.route('/')
def first():
    return redirect('search')
'''
@app.route('/search?<input>')
def outfile(input):
    x = input.split('=')
    b = x[1]
    with open('products.csv', 'r') as infile:
        a = infile.readlines()
    plist = []
    for line in a:
        xx = line.split(';')
        plist.append(xx)
    for i in range(len(plist)):
        if b in plist[i]:
            return 'ID: '+plist[i][0]+' Name: '+plist[i][1]+' Price: '+plist[i][2]+' Quantity: '+plist[i][3]
        else:
            return 'We do not have the Product'
'''
if __name__ == '__main__':
    app.run(debug=True)