from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(420), nullable=False)


class DBBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(420), nullable=False)
    total = db.Column(db.Integer, nullable=False)
    available = db.Column(db.Integer, nullable=False)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(240), nullable=False)


class BorrowedBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookid = db.Column(db.Integer, nullable=False)
    personid = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
