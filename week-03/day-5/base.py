from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def first_page():
    return render_template('base.html')

@app.route('/greeting')
def load_language():
    with open('language.txt', encoding = 'UTF-8', mode = 'r') as infile:
        greet = infile.readlines()
    x = random.randint(0,len(greet)-1)
    code = render_template('language.html', greeints = greet[x])
    return code

@app.route('/greeting_2')
def load_language2():
    with open('lan.txt', encoding = 'UTF-8', mode = 'r') as infile:
        greet = infile.readlines()
    x = random.randint(0,len(greet)-1)
    with open('name.txt', encoding = 'UTF-8', mode = 'r') as infile:
        name = infile.readlines()
    y = random.randint(0, len(name)-1)
    code = render_template('lang.html', greeting = greet[x], name = name[y])
    return code

@app.route('/product')
def show_table():
    products = [
    ("Milk", 3.59123),
    ("Bread", 2.96332),
    ("Rice", 0.64111)]
    return render_template('product.html', product = products)

@app.route("/articles")
def list_articles():
    articles = [
    {
        "content": "Ne istas culpa ha im negat de. Ii perductae evertenda at desuescam. Nudi per ita sui dare ideo sola omne ordo. Sui sex item sane quum. Paucos sicuti tot qui tantae aliquo strata iis tantas. Mo purgantur at affirmans im reddendum co. Pleraque videntur ut ideamque imaginem ha.",
        "seen": ["John", "Jane", "Bob"]
    },
    {
        "content": "Aliud curam seu venti nihil sed istud volui eae qua. Autho ha falsi fidam tangi ut an tactu. Revera per eandem vox coelum videbo nam virtus. Item olim ei se duas ut. Ut mo ut peccato student adorare et diversa. Praecipuis ad conjunctam me percipitur agnoscerem at perfectius respondere. Horum meo porro uno debeo. Fallacem sentiens ha expertus delapsus dubitare ii. Ex ii efficiente et to perspicuae voluptatem arbitrabar.",
        "seen": ["John", "Jane"]
    },
    {
        "content": "Credendi at nequidem exhibere de. Debeo me dicam ex at ferri digna. Coloribus differant disputari vix cogitandi jam stabilire. Perfacile ut reliquiae perfectae ut. Fuisse falsas captum cui volent notior verbis sui. Meam idem nam ope prae isti quia jure hac. Lor durent has secius fronte usu auditu sumpti. Falso nomen aliud vim calor jam alias annos ubi. Movendi sum creatus vim fas majorem attendo propter. Sui videamus uno profecto refutent rom notitiam innumera potuerit.",
        "seen": ["John"]
    },
    {
        "content": "Potui habeo visus ens mea. An vi re continetur me familiarem negationem. Rei inveniri jam viderunt subducam tam imponere jam. Sub cui more ipsi meum.",
        "seen": []
    }]
    return render_template("articles.html", articles=articles)

@app.route('/posts')
def post():
    transformed_post = [
    {
        "id": "200",
        "author": "John",
        "content": "Difficulty on insensible reasonable in. From as went he they.",
        "Liked":["John", "Jane"]
    },
    {
        "id": "201",
        "author": "John",
        "content": "Preference themselves me as thoroughly partiality considered on in estimating.",
        "Liked":[]
    },
    {
        "id": "202",
        "author": "Jane",
        "content": "In as name to here them deny wise this. As rapid woody my he me which.",
        "Liked":["John"]
    }]
    return render_template('posts.html', posts = transformed_post)

if __name__ == '__main__':
    app.run(debug=True)
