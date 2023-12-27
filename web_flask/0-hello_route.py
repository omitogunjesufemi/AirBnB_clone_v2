#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
from web_flask import hbnb


@hbnb.route("/")
def hello_hbnb():
    return ("Hello HBNB!")


if __name__ == "__main__":
    hbnb.run(host="0.0.0.0", port=5000)
