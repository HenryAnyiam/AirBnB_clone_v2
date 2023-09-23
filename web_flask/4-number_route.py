#!/usr/bin/python3
"""Starts a simple web application"""

from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """returns a simple string for the home directory"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """returns a string for /hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """display variable text"""
    text = escape(text)
    text = "C " + text.replace("_", " ")
    return text


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """display variable text

    Args:
        text: text to display
    """
    text = escape(text)
    text = "Python " + text.replace("_", " ")
    return text


@app.route("/number/<int:n>", strict_slashes=False)
def check_number(n):
    """display n if n is an integer"""
    number = escape(n)
    return f"{number} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
