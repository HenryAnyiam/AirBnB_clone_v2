#!/usr/bin/python3
"""building AirBnB web framework"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_states():
    return render_template("7-states_list.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)