from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


USERNAME = "a"
PASSWORD = ""


@app.route('/auth')
def auth():
    username = request.args.get("username")
    password = request.args.get("password")
    return username == USERNAME and password == PASSWORD
