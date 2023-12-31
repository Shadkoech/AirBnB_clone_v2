#!/usr/bin/python3
"""
Script that starts a web flask
Web app listens on 0.0.0.0,port 5000
Uses storage to fetch data
Route:
    /states_list:display a HTML page
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


@app.route("/states_list", strict_slashes=False)
def list_states():
    """Route handler for /states_list
    obtains all the states created in storage
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
