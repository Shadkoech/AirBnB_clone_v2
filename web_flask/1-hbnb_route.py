#!/usr/bin/python3
"""
Script that starts a web flask
Web app listens on 0.0.0.0 and port 5000
routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Route handled for the root path ("/") of the web flask
    When a request is made to the root, the function is invoked
    """
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Route handler for path /hbnb
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
