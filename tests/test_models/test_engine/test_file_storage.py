#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models import storage
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    @unittest.skipIf(type(storage) == DBStorage,
                     "Testing FileStorage")
    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    @unittest.skipIf(type(storage) == DBStorage,
                     "Testing FileStorage")
    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except Exception as e:
            pass

    @unittest.skipIf(type(storage) == FileStorage,
                     "Testing FileStorage")
    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    @unittest.skipIf(type(storage) == DBStorage,
                     "Testing FileStorage")
    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        new.save()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    @unittest.skipIf(type(storage) == DBStorage,
                     "Testing FileStorage")
    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    @unittest.skipIf(type(storage) == DBStorage,
                     "Testing FileStorage")
    def test_all_with_parameter(self):
        """Class __objects matching the parameter is properly returned """
        new = BaseModel()
        temp = storage.all(BaseModel)
        self.assertIsInstance(temp, dict)

    @unittest.skipIf(type(storage) == DBStorage,
                     "Testing FileStorage")
    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    @unittest.skipIf(type(storage) == DBStorage,
                     "Testing FileStorage")
    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    @unittest.skipIf(type(storage) == DBStorage,
                     "Testing FileStorage")
    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    @unittest.skipIf(type(storage) == DBStorage,
                     "Testing FileStorage")
    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        new.save()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    @unittest.skipIf(type(storage) == DBStorage,
                     "Testing FileStorage")
    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    @unittest.skipIf(type(storage) == DBStorage,
                     "Testing FileStorage")
    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    @unittest.skipIf(type(storage) == DBStorage,
                     "Testing FileStorage")
    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    @unittest.skipIf(type(storage) == DBStorage,
                     "Testing FileStorage")
    def test_delete_obj(self):
        """Delete obj from __objects if obj is not None """
        new = BaseModel()
        new.save()
        new_1 = State()
        new_1.name = "California"
        new_1.save()
        new_2 = State()
        new_2.name = "Nevada"
        new_2.save()
        storage.save()
        self.assertEqual(len(storage.all()), 3)
        storage.delete(new_1)
        self.assertEqual(len(storage.all()), 2)

    @unittest.skipIf(type(storage) == DBStorage,
                     "Testing FileStorage")
    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    @unittest.skipIf(type(storage) == DBStorage,
                     "Testing FileStorage")
    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    @unittest.skipIf(type(storage) == DBStorage,
                     "Testing FileStorage")
    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        new.save()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    @unittest.skipIf(type(storage) == DBStorage,
                     "Testing FileStorage")
    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        self.assertEqual(type(storage), FileStorage)
