#!/usr/bin/python3
"""Testing Class User"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """The defined class with different cases to test User class"""
    def test_user_attributes(self):
        """Test the existence of User attributes"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))

    def test_user_attributes_default_values(self):
        """Test that the default values of User attributes are empty strings"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")

    def test_user_attributes_assignment(self):
        """Test assigning values to User attributes"""
        user = User()
        user.email = "user@example.com"
        user.password = "password123"
        user.first_name = "John"
        self.assertEqual(user.email, "user@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")

    def test_is_subclass(self):
        """Test if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))


    def test_save_method(self):
        """Test the inherited save method"""
        user = User()
        original_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(user.updated_at, original_updated_at)

    def test_to_dict_method(self):
        """Test that the to_dict() method returns a dictionary"""
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)

    def test_str_method(self):
        """Test the string representation of the User object"""
        user = User()
        user_str = str(user)
        self.assertIn('User', user_str)


if __name__ == '__main__':
    unittest.main()
