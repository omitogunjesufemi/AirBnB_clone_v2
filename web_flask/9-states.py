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


@app.route("/states", strict_slashes=False)
def states():
    """ Display HTML page with all States """
    states = storage.all(State)
    return render_template("9-states.html", states=states, state_id="None")


@app.route("/states/<string:id>", strict_slashes=False)
def state_with_id(id):
    """ Display HTML page with a particular state and all its cities """
    states = storage.all(State)
    for state in states.values():
        if state.id == id:
            state = state
            break
        else:
            state = "None"
    return render_template("9-states.html", state=state, state_id=id)


@app.teardown_appcontext
def remove_session(exception=None):
    """ Removes the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
