from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "admin"

books = [
    {"name": "title1", "description": "description1", "catgory": "category1", "author": "author1"},
    {"name": "title2", "description": "description2", "catgory": "category2", "author": "author2"}
]
.
@app.route('/')
def login():
    return render_template('login.html')


@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/wrong_login')
def wrong_login():
    return render_template('wrong_login.html')


@app.route('/dologin', methods=['POST'])
def dologin():
    username = request.form['username']
    password = request.form['password']

    if username == USERNAME and password == PASSWORD:
        return redirect(url_for('books'))
    else:
        return redirect(url_for('wrong_login'))


if __name__ == "__main__":
    app.run()
