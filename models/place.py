#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os

place_amenity = Table(
    "place_amenity", Base.metadata,
    Column("place_id", String(60), ForeignKey("places.id"),
           primary_key=True, nullable=False),
    Column("amenity_id", String(60), ForeignKey("amenities.id"),
           primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review",
                           backref="place",
                           cascade="all, delete, delete-orphan")

    amenities = relationship("Amenity",
                             secondary="place_amenity",
                             overlaps="place_amenities",
                             viewonly=False)

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """ """
            from models import storage
            review_list = []
            for value in list(storage.all(Review).values()):
                if self.id == value.place_id:
                    review_list.append(value)
            return review_list

        @property
        def amenities(self):
            """ """
            from models import storage
            amenities_list = []
            for amenity in list(storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            """Set amenities for FileStorage"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
