from flask import Flask, render_template, redirect, url_for, request, jsonify
from models import db, DBBook, Person, BorrowedBook
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
    # Book.query.delete()
    # db.session.commit()

    if not DBBook.query.first():
        for b in bookdb:
            db.session.add(
                DBBook(
                    title=b["title"],
                    author=b["author"],
                    category=b["category"],
                    description=b["description"],
                    total=4,
                    available=4
                ))
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


@app.route('/newbook')
def newbook():
    return render_template('newbook.html')


@app.route('/newperson')
def newperson():
    return render_template('newperson.html')


@app.route('/borrowbook')
def borrowbook():
    return render_template('borrowbook.html')


def searchBooks(query):
    results = DBBook.query.filter(
        or_(
            DBBook.category.ilike(f"%{query}%"),
            DBBook.author.ilike(f"%{query}%"),
            DBBook.title.ilike(f"%{query}%"),
            DBBook.description.ilike(f"%{query}%")
        )
    ).all()

    return [
        {"title": b.title, "author": b.author, "category": b.category,
         "description": b.description, "total": b.total, "available": b.available}
        for b in results
    ]


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get("query")

    bookResults = searchBooks(query)
    return render_template("books.html", bookResults=bookResults)


@app.route('/addbook', methods=['POST'])
def addbook():
    title = request.form.get("title")
    author = request.form.get("author")
    description = request.form.get("description")
    category = request.form.get("category")
    number = request.form.get("number")

    db.session.add(
        DBBook(
            title=title,
            author=author,
            category=category,
            description=description,
            total=int(number),
            available=int(number)
        ))


    db.session.commit()
    return render_template("addsuccess.html")

@app.route('/addperson', methods=['POST'])
def addperson():
    name = request.form.get("name")
    address = request.form.get("address")

    db.session.add(
        Person(
            name=name,
            address=address
        ))


    db.session.commit()
    return render_template("addPersonSuccess.html")


@app.route('/borrow', methods=['POST'])
def borrow():
    bookid = request.form.get("bookid")
    personid = request.form.get("personid")

    db.session.add(
        BorrowedBook(
            bookid=bookid,
            personid=personid
        ))


    db.session.commit()
    return render_template("borrowSuccess.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
