#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    @unittest.skip("Doesn't support the current ORM model")
    def test_state_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_name3(self):
        """ """
        new = self.value()
        new.name = "California"
        self.assertEqual(type(new.name), str)
