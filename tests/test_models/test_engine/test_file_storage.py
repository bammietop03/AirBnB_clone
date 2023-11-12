#!/usr/bin/python3
"""
Unit tests using the unittest module to test the functionality
of the FileStorage class.
"""
import unittest
import os
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
        print(f"Teardown: Full path: {full_path}")

        if os.path.exists(full_path):
            print(f"Teardown: Removing file at {full_path}")
            os.remove(full_path)
        else:
            print(f"Teardown: File does not exist at {full_path}")


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


if __name__ == '__main__':
    unittest.main()
