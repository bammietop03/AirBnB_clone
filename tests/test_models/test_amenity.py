#!/usr/bin/python3
"""Defines unittests for models/amenity.py"""
import unittest
from models.amenity import Amenity
from datetime import datetime
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def setUp(self):
        """Set up a new Amenity instance for each test."""
        self.amenity = Amenity()

    def test_attributes(self):
        """Test the existence of required attributes."""
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_id_generation(self):
        """Test the generation of a unique ID."""
        self.assertIsNotNone(self.amenity.id)
        self.assertEqual(len(self.amenity.id), 36)

    def test_created_at_type(self):
        """Test the type of the 'created_at' attribute."""
        self.assertIsInstance(self.amenity.created_at, datetime)

    def test_updated_at_type(self):
        """Test the type of the 'updated_at' attribute."""
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_name_default_value(self):
        """Test the default value of the 'name' attribute."""
        self.assertEqual(self.amenity.name, "")

    def test_amenity_attributes_assignment(self):
        """ Test assigning values to Amenity attributes """
        self.amenity.name = "John"
        self.assertEqual(self.amenity.name, "John")

    def test_is_subclass(self):
        """Test if Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_save_method(self):
        """Test the 'save' method for updating 'updated_at'."""
        initial_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(initial_updated_at, self.amenity.updated_at)

    def test_to_dict_method(self):
        """Test the 'to_dict' method for generating a dictionary."""
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['id'], self.amenity.id)
        self.assertEqual(amenity_dict['created_at'],
                         self.amenity.created_at.isoformat())
        self.assertEqual(amenity_dict['updated_at'],
                         self.amenity.updated_at.isoformat())

    def test_str_method(self):
        """Test the '__str__' method for generating a string representation."""
        str_representation = str(self.amenity)
        self.assertIn(self.amenity.__class__.__name__, str_representation)
        self.assertIn(self.amenity.id, str_representation)
        self.assertIn(str(self.amenity.__dict__), str_representation)


if __name__ == '__main__':
    unittest.main()
