#!/usr/bin/python3
"""unittest State"""
import unittest
from models.state import State
from datetime import datetime
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def setUp(self):
        """Set up a new State instance for each test."""
        self.state = State()

    def test_attributes(self):
        """Test the existence of required attributes."""
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))
        self.assertTrue(hasattr(self.state, 'name'))

    def test_id_generation(self):
        """Test the generation of a unique ID."""
        self.assertIsNotNone(self.state.id)
        self.assertEqual(len(self.state.id), 36)

    def test_created_at_type(self):
        """Test the type of the 'created_at' attribute."""
        self.assertIsInstance(self.state.created_at, datetime)

    def test_updated_at_type(self):
        """Test the type of the 'updated_at' attribute."""
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_name_default_value(self):
        """Test the default value of the 'name' attribute."""
        self.assertEqual(self.state.name, "")

    def test_is_subclass(self):
        """Test if State is a subclass of BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_attributes_assignment(self):
        """ Test assigning values to State attributes """
        self.state.name = "John"
        self.assertEqual(self.state.name, "John")

    def test_save_method(self):
        """Test the 'save' method for updating 'updated_at'."""
        initial_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(initial_updated_at, self.state.updated_at)

    def test_to_dict_method(self):
        """Test the 'to_dict' method for generating a dictionary."""
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['id'], self.state.id)
        self.assertEqual(state_dict['created_at'],
                         self.state.created_at.isoformat())
        self.assertEqual(state_dict['updated_at'],
                         self.state.updated_at.isoformat())

    def test_str_method(self):
        """Test the '__str__' method for generating a string representation."""
        str_representation = str(self.state)
        self.assertIn(self.state.__class__.__name__, str_representation)
        self.assertIn(self.state.id, str_representation)
        self.assertIn(str(self.state.__dict__), str_representation)


if __name__ == '__main__':
    unittest.main()
