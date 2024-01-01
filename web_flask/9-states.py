#!/usr/bin/python3
"""
Script that starts a web flask
Web app listens on 0.0.0.0,port 5000
Uses storage to fetch data
Route:
    /states: display a HTML page
    /states/<id>: display a HTML page
"""

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """Closes and removes the running SQLAlchemy session
    """
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """Route handler for /states
    Display HTML page with all the states
    """
    states = storage.all("State")
    return render_template("9-states.html", states=states, mode='all')


@app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    """Displays an HTML page with infomation on ID
    """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", states=state, mode='id')
        return render_template("9-states.html", states=state)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
