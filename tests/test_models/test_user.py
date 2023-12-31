#!/usr/bin/python3
"""Testing Class User"""
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):
    """The defined class with different cases to test User class"""
    def test_user_attributes(self):
        """Test the existence of User attributes"""
        self.user = User()
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))

    def test_user_attributes_default_values(self):
        """Test that the default values of User attributes are empty strings"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_attributes_assignment(self):
        """Test assigning values to User attributes"""
        user = User()
        user.email = "user@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Edwards"
        self.assertEqual(user.email, "user@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Edwards")

    def test_is_subclass(self):
        """Test if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_save_method(self):
        """Test the inherited save method"""
        user = User()
        original_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(user.updated_at, original_updated_at)

    def test_to_dict_method(self):
        """Test that the to_dict() method returns a dictionary"""
        self.user = User()
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['id'], self.user.id)
        self.assertEqual(user_dict['created_at'],
                         self.user.created_at.isoformat())
        self.assertEqual(user_dict['updated_at'],
                         self.user.updated_at.isoformat())

    def test_str_method(self):
        """Test the string representation of the User object"""
        self.user = User()
        user_str = str(self.user)
        self.assertIn('User', user_str)
        self.assertIn(self.user.__class__.__name__, user_str)
        self.assertIn(self.user.id, user_str)
        self.assertIn(str(self.user.__dict__), user_str)

    def test_id_generation(self):
        """Test the generation of a unique ID."""
        self.user = User()
        self.assertIsNotNone(self.user.id)
        self.assertEqual(len(self.user.id), 36)

    def test_created_at_type(self):
        """Test the type of the 'created_at' attribute."""
        self.user = User()
        self.assertIsInstance(self.user.created_at, datetime)

    def test_updated_at_type(self):
        """Test the type of the 'updated_at' attribute."""
        self.user = User()
        self.assertIsInstance(self.user.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
