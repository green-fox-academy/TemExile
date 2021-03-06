from flask import Flask, render_template

app = Flask(__name__)
authors = [
    {
        "id": 100,
        "name": "John",
        "likes": [
            202,
            200
        ]
    },
    {
        "id": 101,
        "name": "jane",
        "likes" : [
            200
        ]
    }]
posts = [
    {
        "id": 200,
        "author": 100,
        "content": "Difficulty on insensible reasonable in. From as went he they."
    },
    {
        "id": 201,
        "author": 100,
        "content": "Preference themselves me as thoroughly partiality considered on in estimating."
    },
    {
        "id": 202,
        "author": 101,
        "content": "In as name to here them deny wise this. As rapid woody my he me which."
    }]
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
