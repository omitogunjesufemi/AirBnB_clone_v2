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
from models.city import City

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """ Display HTML with cities inside their states """
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def remove_session(exception=None):
    """ Removes the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
