#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Getter for cities attribute when in fileStorage """
            cities_list = []
            from models import storage
            all_cities = storage.all(City)
            for key, value in all_cities.items():
                if (value.state_id == self.id):
                    cities_list.append(value)
            return cities_list
