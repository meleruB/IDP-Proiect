from flask import Flask, render_template, redirect, url_for, request, jsonify
from models import db, Book
from sqlalchemy import or_

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:secret@db:5432/app_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

bookdb = [
    {"title": "Ocolul pamantului in 80 de zile", "description": "description1", "category": "SF", "author": "Jules Verne"},
    {"title": "Ocolul Lunii", "description": "description1", "category": "SF", "author": "Jules Verne"},
    {"title": "Roman", "description": "description2", "category": "action", "author": "Mihai Ionescu"}
]

with app.app_context():
    db.create_all()

    if not Book.query.first():
        for b in bookdb:
            db.session.add(Book(title=b["title"], author=b["author"], category=b["category"], description=b["description"]))
        db.session.commit()


USERNAME = "a"
PASSWORD = ""

categories = [
    "category1", "category2"
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
    results = Book.query.filter(
        or_(
            Book.category.ilike(f"%{query}%"),
            Book.author.ilike(f"%{query}%"),
            Book.title.ilike(f"%{query}%"),
            Book.description.ilike(f"%{query}%")
        )
    ).all()

    return [
        {"title": b.title, "author": b.author, "category": b.category, "description": b.description}
        for b in results
    ]


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get("query")

    bookResults = searchBooks(query)
    return render_template("books.html", bookResults=bookResults)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
