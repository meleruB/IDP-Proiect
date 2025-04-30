from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

USERNAME = "a"
PASSWORD = ""

categories = [
    "category1", "category2"
]

bookdb = [
    {"title": "Ocolul pamantului in 80 de zile", "description": "description1", "category": "SF", "author": "Jules Verne"},
    {"title": "Ocolul Lunii", "description": "description1", "category": "SF",
     "author": "Jules Verne"},
    {"title": "Roman", "description": "description2", "category": "action", "author": "Mihai Ionescu"}
]

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


def searchBooks(query):
    result = []
    words = query.lower().split(" ")
    for word in words:
        for book in bookdb:
            if (
                    word in book.get("title").lower()
                    or word in book.get("author").lower()
                    or word in book.get("description").lower()
                    or word in book.get("category").lower()
            ):
                result.append(book)
    return result


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get("query")

    bookResults = searchBooks(query)
    return render_template("books.html", bookResults=bookResults)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
