from flask import Flask,render_template
from datetime import datetime

app = Flask("hello")

posts = [
    {
        'title': 'O meu primeiro Post',
        'body': 'Aqui é o texto do post',
        'author': 'Yuri',
        'created' : datetime(2022,7,25)

    },
    {
        'title': 'Segundo Post',
        'body': 'Aqui é o texto do post',
        'author': 'Camilla',
        'created' : datetime(2022,7,26)

    }
]

@app.route("/")
def index():
    return render_template('index.html', posts=posts)

@app.route('/login')
def login():
    return render_template('login.html')







