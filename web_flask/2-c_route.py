#!/usr/bin/python3
"""
A script that starts a Flask web application
Listening on 0.0.0.0, port 5000

Routes:
   /: displays Hello HBNB!
   /hbnb: displays HBNB
   /c/<text>: display C followed by the value of the text variable
   (replace underscore _ symbols with a space
"""
from flask import Flask

hbnb = Flask(__name__)


@hbnb.route("/", strict_slashes=False)
def hello_hbnb():
    """ Displays Hello HBNB! """
    return ("Hello HBNB!")


@hbnb.route("/hbnb", strict_slashes=False)
def hbnb_print():
    """ Displays HBNB """
    return ("HBNB")


@hbnb.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """Displays C follow by value of text """
    text = text.replace("_", " ")
    return (f"C {text}")


if __name__ == "__main__":
    hbnb.run(host="0.0.0.0", port=5000)
