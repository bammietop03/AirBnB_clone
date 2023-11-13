#!/usr/bin/python3
"""
Unit tests using the unittest module to test the functionality
of the FileStorage class.
"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    def setUp(self):
        """
        The setUp method is called before each test case is executed.
        It sets up the necessary environment for the tests.

        self.file_path: Specifies the path to the test file.
        self.storage: Creates an instance of the FileStorage class.
        self.storage._FileStorage__file_path: Sets the file path of
                    the storage instance to the test file path.
        """
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        storage.all().clear()

    def tearDown(self):
        """
        The tearDown method is called after each test case is executed.
        It cleans up any artifacts created during testing.

        Checks if the test file exists and removes it if it does.
        """
        full_path = os.path.abspath(self.file_path)
        if os.path.exists(full_path):
            os.remove(full_path)

    def test_all(self):
        """ testing if self.storage.all() is an instance of dict"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """
        1. Create some test objects
        2. Add objects to storage
        3. Save and reload storage
        4. Check if objects are present in reloaded storage
        """
        obj1 = BaseModel()
        obj2 = User()
        obj3 = State()
        obj4 = City()
        obj5 = Amenity()
        obj6 = Place()
        obj7 = Review()

        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.new(obj3)
        self.storage.new(obj4)
        self.storage.new(obj5)
        self.storage.new(obj6)
        self.storage.new(obj7)

        self.storage.save()
        self.storage.reload()

        all_objects = self.storage.all()
        self.assertIn(f"BaseModel.{obj1.id}", all_objects)
        self.assertIn(f"User.{obj2.id}", all_objects)
        self.assertIn(f"State.{obj3.id}", all_objects)
        self.assertIn(f"City.{obj4.id}", all_objects)
        self.assertIn(f"Amenity.{obj5.id}", all_objects)
        self.assertIn(f"Place.{obj6.id}", all_objects)
        self.assertIn(f"Review.{obj7.id}", all_objects)

    def test_save_reload(self):
        """
        1. Create some test objects
        2. Add objects to storage
        3. Save and reload storage
        4. Check if objects are present in reloaded storage
        """
        obj1 = BaseModel()
        obj2 = User()
        obj3 = State()
        obj4 = City()
        obj5 = Amenity()
        obj6 = Place()
        obj7 = Review()

        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.new(obj3)
        self.storage.new(obj4)
        self.storage.new(obj5)
        self.storage.new(obj6)
        self.storage.new(obj7)

        self.storage.save()
        self.storage.reload()

        all_objects = self.storage.all()
        self.assertIn(f"BaseModel.{obj1.id}", all_objects)
        self.assertIn(f"User.{obj2.id}", all_objects)
        self.assertIn(f"State.{obj3.id}", all_objects)
        self.assertIn(f"City.{obj4.id}", all_objects)
        self.assertIn(f"Amenity.{obj5.id}", all_objects)
        self.assertIn(f"Place.{obj6.id}", all_objects)
        self.assertIn(f"Review.{obj7.id}", all_objects)
        self.assertIsInstance(all_objects, dict)

    def test_all_empty_storage(self):
        """ Test 'all' method when storage is empty"""
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 0)
        self.assertIsInstance(all_objects, dict)

    def test_all_with_arg(self):
        """test all with none"""
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new_with_args(self):
        """ testing new with args """
        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        """ testing new with none """
        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_save_with_none(self):
        """ testing save with none """
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload_with_none(self):
        """testing reload with none """
        with self.assertRaises(TypeError):
            storage.reload(None)

    def test_FileStorage_no_args(self):
        """testing FileStorage with no args"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_with_arg(self):
        """testing FileStorage with args"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        """testing file_path is a private str"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_objects_is_private_dict(self):
        """testing file_path is private dict"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage(self):
        """testing storage """
        self.assertEqual(type(storage), FileStorage)

    def test_reload_existing_file(self):
        """Test reloading from an existing file"""
        user = User()
        self.storage.new(user)
        self.storage.save()
        self.storage.reload()
        objects = self.storage.all()
        self.assertIn('User.{}'.format(user.id), objects)

    def test_reload_nonexistent_file(self):
        """Test reloading from a nonexistent file"""
        self.storage.reload()  # Should not raise an exception

    def test_reload_empty_file(self):
        """Test reloading from an empty file"""
        with open(self.storage._FileStorage__file_path, 'w',
                  encoding='utf-8') as file:
            file.write('{}')
        self.storage.reload()  # Should not raise an exception

    def test_reload_invalid_file(self):
        """Test reloading from an invalid JSON file"""
        with open(self.storage._FileStorage__file_path, 'w',
                  encoding='utf-8') as file:
            file.write('invalid json')
        with self.assertRaises(json.JSONDecodeError):
            self.storage.reload()


if __name__ == '__main__':
    unittest.main()
