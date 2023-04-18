import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    name = os.getenv("NAME", "World")
    return f"Hello, {name}!"


@app.route("/about")
def about():
    return "About Us"
