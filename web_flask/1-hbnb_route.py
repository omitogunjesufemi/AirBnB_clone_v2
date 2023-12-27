#!/usr/bin/python3
"""
"""
from flask import Flask

hbnb = Flask(__name__)


@hbnb.route("/", strict_slashes=False)
@hbnb.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """Route to display Hello HBNB!"""
    return ("Hello HBNB!")


@hbnb.route("/hbnb", strict_slashes=False)
def hbnb():
    """Route to display Hello HBNB!"""
    return ("HBNB!")


if __name__ == "__main__":
    hbnb.run(host="0.0.0.0", port=5000)
