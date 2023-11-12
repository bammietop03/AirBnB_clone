#!/usr/bin/python3
"""Tests class city"""
import unittest
from models.city import City
from datetime import datetime
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """The defined class with different cases to test City class"""
    def setUp(self):
        """Set up a new City instance for each test."""
        self.city = City()

    def test_attributes(self):
        """Test the existence of required attributes."""
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_id_generation(self):
        """Test the generation of a unique ID."""
        self.assertIsNotNone(self.city.id)
        self.assertEqual(len(self.city.id), 36)

    def test_created_at_type(self):
        """Test the type of the 'created_at' attribute."""
        self.assertIsInstance(self.city.created_at, datetime)

    def test_updated_at_type(self):
        """Test the type of the 'updated_at' attribute."""
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_state_id_default_value(self):
        """Test the default value of the 'state_id' attribute."""
        self.assertEqual(self.city.state_id, "")

    def test_name_default_value(self):
        """Test the default value of the 'name' attribute."""
        self.assertEqual(self.city.name, "")

    def test_city_attributes_assignment(self):
        """ Test assigning values to city attributes """
        self.city.name = "John"
        self.city.state_id = "123"
        self.assertEqual(self.city.name, "John")
        self.assertEqual(self.city.state_id, "123")

    def test_is_subclass(self):
        """Test if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_save_method(self):
        """Test the 'save' method for updating 'updated_at'."""
        initial_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(initial_updated_at, self.city.updated_at)

    def test_to_dict_method(self):
        """Test the 'to_dict' method for generating a dictionary."""
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['id'], self.city.id)
        self.assertEqual(city_dict['created_at'],
                         self.city.created_at.isoformat())
        self.assertEqual(city_dict['updated_at'],
                         self.city.updated_at.isoformat())

    def test_str_method(self):
        """Test the '__str__' method for generating a string representation."""
        str_representation = str(self.city)
        self.assertIn(self.city.__class__.__name__, str_representation)
        self.assertIn(self.city.id, str_representation)
        self.assertIn(str(self.city.__dict__), str_representation)


if __name__ == '__main__':
    unittest.main()
