#!/usr/bin/python3
"""
Script that starts a web flask
Web app listens on 0.0.0.0,port 5000
Uses storage to fetch data
Route:
    /hbnb_filters: display a HTML page like 6-index.html,
    which was done during the project 0x01. AirBnB clone - Web static
"""

from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """Closes and removes the running SQLAlchemy session
    """
    storage.close()


@app.route('/hbnb_filters/', strict_slashes=False)
def hbnb_filter():
    """ handles /hbnb_filters route """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
