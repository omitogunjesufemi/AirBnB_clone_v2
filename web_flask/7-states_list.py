#!/usr/bin/python3
"""
A script that starts a Flask web application
Listening on 0.0.0.0, port 5000

Routes:
   /states_list: display a HTML page inside the tag BODY
       - H1 tag: "States"
       - UL tag: with the list of all State objects present in DBStorage
                 sorted by name (A->Z) tip
       - LI tag: description of one State: <state.id>:
                 <B><state.name></B>
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ Display a HTML page with list of States """
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def remove_session(exception=None):
    """ Removes the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
