#!/usr/bin/python3
""" Module for testing database storage"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.user import User
from models.review import Review
from models import storage
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os


class test_dbStorage(unittest.TestCase):
    """Class to test the database storage method """

    def test_all(self):
        """ """
        new = State(name="California")
        new.save()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_new(self):
        """DB Storage new method """
        new = BaseModel()
        storage.new(new)
        storage.save()
        exp_obj = None
        base_models = storage.all(BaseModel)
        for base_model in base_models.values():
            if base_model.id == new.id:
                exp_obj = base_model
        self.assertEqual(new.id, exp_obj.id)

    def test_save(self):
        """ DBStorage save method """
        new = BaseModel()
        new.save()
        storage.save()
        exp_obj = None
        base_models = storage.all(BaseModel)
        for base_model in base_models.values():
            if base_model.id == new.id:
                exp_obj = base_model
        self.assertEqual(new.id, exp_obj.id)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        exp_obj = None
        base_models = storage.all(BaseModel)
        for base_model in base_models.values():
            if base_model.id == new.id:
                exp_obj = base_model
        self.assertEqual(new.id, exp_obj.id)

    def test_delete(self):
        """ """
        new = BaseModel()
        new_1 = State(name="California")
        new_2 = State(name="Nevada")
        new.save()
        new_1.save()
        new_2.save()
        storage.save()
        total_len = len(storage.all())
        self.assertEqual(len(storage.all()), total_len)
        storage.delete(new_1)
        self.assertEqual(len(storage.all()), total_len - 1)

    def test_reload(self):
        """DBStorage Reload method """
        storage.reload()
        total_len = len(storage.all())
        self.assertEqual(len(storage.all()), total_len)
        new = BaseModel()
        new_1 = State(name="California")
        new.save()
        new_1.save()
        storage.reload()
        new_2 = State(name="Nevada")
        self.assertEqual(len(storage.all()), total_len + 2)
        new_2.save()
        self.assertEqual(len(storage.all()), total_len + 3)
