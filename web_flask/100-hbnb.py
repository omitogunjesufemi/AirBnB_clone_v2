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
from models.amenity import Amenity
from models.city import City
from models.place import Place

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Display the AirBnB clone HTML page """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    cities = storage.all(City)
    return render_template("100-hbnb.html", states=states,
                           amenities=amenities, places=places)


@app.teardown_appcontext
def remove_session(exception=None):
    """ Removes the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
