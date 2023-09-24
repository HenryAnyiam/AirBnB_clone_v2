#!/usr/bin/python3
"""building AirBnB web framework"""
from flask import Flask, render_template
from models import storage
from models import *


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_states():
    """list out availablr states"""
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def tear_down(exception=None):
    """close session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
