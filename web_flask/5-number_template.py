#!/usr/bin/python3
"""
A script that starts a Flask web application
Listening on 0.0.0.0, port 5000

Routes:
   /: displays Hello HBNB!
   /hbnb: displays HBNB
   /c/<text>: display C followed by the value of the text variable
   (replace underscore _ symbols with a space)

   /python/<text>: display Python followed by the value of the text
   variable (replace underscore with a space) [text default: is cool]

   /number/<int:n>: display n is a number only if n is an integer

"""
from flask import Flask, render_template, url_for

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


@hbnb.route("/python/", defaults={"text": "is cool"},
            strict_slashes=False)
@hbnb.route("/python/<text>", strict_slashes=False)
def display_python(text):
    """Displays Python follow by value of text """
    text = text.replace("_", " ")
    return (f"Python {text}")


@hbnb.route("/number/<int:n>", strict_slashes=False)
def display_n(n):
    """Displays n is a number only if n is an integer """
    return (f"{n} is a number")


@hbnb.route("/number_template/<int:n>", strict_slashes=False)
def display_number_template(n):
    """Displays a HTML page only if n is an integer """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    hbnb.run(host="0.0.0.0", port=5000)
