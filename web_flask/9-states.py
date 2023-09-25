#!/usr/bin/python3
"""building AirBnB web framework"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models import *


app = Flask(__name__)


@app.route("/states/<id>", strict_slashes=False)
@app.route("/states", strict_slashes=False)
def list_states(id=None):
    """list out availablr states"""
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    if id is None:
        return render_template("7-states_list.html", states=states)
    else:
        id = escape(id)
        for i in states:
            if id == i.id:
                return render_template("9-states.html", states=i)
        return render_template("9-states.html", states="Not found!")


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_state():
    """list out cities by state"""
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    for state in states:
        list(state.cities).sort(key=lambda x: x.name)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def tear_down(exception=None):
    """close session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
