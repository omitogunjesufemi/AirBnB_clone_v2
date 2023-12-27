#!/usr/bin/python3
"""
"""
from flask import Flask

hbnb = Flask(__name__)


@hbnb.route("/")
@hbnb.route("/hbnb")
def hello_hbnb():
    """Route to display Hello HBNB!"""
    return ("Hello HBNB!")


if __name__ == "__main__":
    hbnb.run(host="0.0.0.0", port=5000)
