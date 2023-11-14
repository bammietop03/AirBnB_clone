#!/usr/bin/python3
"""Test Cases for Place class"""
import unittest
from models.place import Place
from datetime import datetime
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """The defined class with different cases to test Place class"""
    def setUp(self):
        """Set up a new Place instance for each test."""
        self.place = Place()

    def test_attributes(self):
        """Test the existence of required attributes."""
        self.assertTrue(hasattr(self.place, 'id'))
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_id_generation(self):
        """Test the generation of a unique ID."""
        self.assertIsNotNone(self.place.id)
        self.assertEqual(len(self.place.id), 36)

    def test_created_at_type(self):
        """Test the type of the 'created_at' attribute."""
        self.assertIsInstance(self.place.created_at, datetime)

    def test_updated_at_type(self):
        """Test the type of the 'updated_at' attribute."""
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_city_id_default_value(self):
        """Test the default value of the 'city_id' attribute."""
        self.assertEqual(self.place.city_id, "")

    def test_user_id_default_value(self):
        """Test the default value of the 'user_id' attribute."""
        self.assertEqual(self.place.user_id, "")

    def test_name_default_value(self):
        """Test the default value of the 'name' attribute."""
        self.assertEqual(self.place.name, "")

    def test_description_default_value(self):
        """Test the default value of the 'description' attribute."""
        self.assertEqual(self.place.description, "")

    def test_number_rooms_default_value(self):
        """Test the default value of the 'number_rooms' attribute."""
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms_default_value(self):
        """Test the default value of the 'number_bathrooms' attribute."""
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest_default_value(self):
        """Test the default value of the 'max_guest' attribute."""
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night_default_value(self):
        """Test the default value of the 'price_by_night' attribute."""
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude_default_value(self):
        """Test the default value of the 'latitude' attribute."""
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude_default_value(self):
        """Test the default value of the 'longitude' attribute."""
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids_default_value(self):
        """Test the default value of the 'amenity_ids' attribute."""
        self.assertEqual(self.place.amenity_ids, [])

    def test_is_subclass(self):
        """Test if Place is a subclass of BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_place_attributes_assignment(self):
        """ Test assigning values to Place attributes """
        self.place.name = "John"
        self.place.city_id = "Lagos"
        self.place.user_id = "123"
        self.place.description = "Very Tall"
        self.place.number_rooms = 212
        self.place.number_bathrooms = 230
        self.place.max_guest = 50
        self.place.price_by_night = 2500
        self.place.latitude = 45323.2
        self.place.longitude = 4534.1
        self.place.amenity_ids = [234343, 444424]
        self.assertEqual(self.place.name, "John")
        self.assertEqual(self.place.city_id, "Lagos")
        self.assertEqual(self.place.user_id, "123")
        self.assertEqual(self.place.description, "Very Tall")
        self.assertEqual(self.place.number_rooms, 212)
        self.assertEqual(self.place.number_bathrooms, 230)
        self.assertEqual(self.place.max_guest, 50)
        self.assertEqual(self.place.price_by_night, 2500)
        self.assertEqual(self.place.latitude, 45323.2)
        self.assertEqual(self.place.longitude, 4534.1)
        self.assertEqual(self.place.amenity_ids, [234343, 444424])

    def test_save_method(self):
        """Test the 'save' method for updating 'updated_at'."""
        initial_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(initial_updated_at, self.place.updated_at)

    def test_to_dict_method(self):
        """Test the 'to_dict' method for generating a dictionary."""
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['id'], self.place.id)
        self.assertEqual(place_dict['created_at'],
                         self.place.created_at.isoformat())
        self.assertEqual(place_dict['updated_at'],
                         self.place.updated_at.isoformat())

    def test_str_method(self):
        """Test the '__str__' method for generating a string representation."""
        str_representation = str(self.place)
        self.assertIn(self.place.__class__.__name__, str_representation)
        self.assertIn(self.place.id, str_representation)
        self.assertIn(str(self.place.__dict__), str_representation)


if __name__ == '__main__':
    unittest.main()
