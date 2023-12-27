#!/usr/bin/python3
"""This initializes the app
"""
from flask import Flask


hbnb = Flask(__name__)
hbnb.url_map.strict_slashes = False
