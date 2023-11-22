#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import unittest


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    @unittest.skip("Doesn't support the ORM")
    def test_user_first_name(self):
        """ """
        new = self.value()
        new.first_name = "Jesufemi"
        self.assertEqual(type(new.first_name), str)

    def test_first_name(self):
        """ """
        new = self.value()
        new.first_name = "Jesufemi"
        self.assertEqual(type(new.first_name), str)

    @unittest.skip("Doesn't support the ORM")
    def test_user_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        new.last_name = ""
        self.assertEqual(type(new.last_name), str)

    @unittest.skip("Doesn't support the ORM")
    def test_user_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_email(self):
        """ """
        new = self.value()
        new.email = "jf@hbn.io"
        self.assertEqual(type(new.email), str)

    @unittest.skip("Doesn't support the ORM")
    def test_user_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)

    def test_password(self):
        """ """
        new = self.value()
        new.password = "omix1234"
        self.assertEqual(type(new.password), str)
