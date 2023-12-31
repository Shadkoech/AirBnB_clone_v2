#!/usr/bin/python3
"""
Script that starts a web flask
Web app listens on 0.0.0.0,port 5000
Uses storage to fetch data
Route:
    /cities_by_states:display a HTML page
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


@app.route("/cities_by_states", strict_slashes=False)
def list_cities():
    """Route handler for /states_list
    obtains all the cities and their states in storage
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
