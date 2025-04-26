from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/recommend')
def recommend():
    return {"title": "Ocolul pamantului in 80 de zile", "description": "description1", "category": "SF", "author": "Jules Verne"}
