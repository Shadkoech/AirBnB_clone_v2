#!/usr/bin/python3
"""
Script that starts a web flask
Web app listens on 0.0.0.0,port 5000
routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of <text> variable
    /python/<text>: display "Python followed by value of text variable
    /number/<n>: displays "n is a number” only if n is an integer"
    /number_template/<n>: displays a HTML page only if n is an integer
    //number_odd_or_even/<n>: displays a HTML page only of n is int
"""

from flask import Flask
from flask import render_template

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


@app.route("/c/<text>", strict_slashes=False)
def c_isfun(text):
    """Route handler for the path /c/<text>
    Displays C followed by text variable
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Route handler for /python with and without text
    Displays Python followed by text
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Router handler for /number/<n>
    When accessed displays 'n is a number' only if n is an integer
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Route handler for /number_template/<n>
    When accessed it displays a HTML body if n is an integer
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """Route handler for path /number_odd_or_even/<n>
    Displays an HTML body in n is an int odd or even
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
