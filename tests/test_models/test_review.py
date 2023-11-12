#!/usr/bin/python3
""" TestCases for Review Class"""
import unittest
from models.review import Review
from datetime import datetime
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """The defined class with different cases to test Review class"""
    def setUp(self):
        """Set up a new Review instance for each test."""
        self.review = Review()

    def test_attributes(self):
        """Test the existence of required attributes."""
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_id_generation(self):
        """Test the generation of a unique ID."""
        self.assertIsNotNone(self.review.id)
        self.assertEqual(len(self.review.id), 36)

    def test_created_at_type(self):
        """Test the type of the 'created_at' attribute."""
        self.assertIsInstance(self.review.created_at, datetime)

    def test_updated_at_type(self):
        """Test the type of the 'updated_at' attribute."""
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_is_subclass(self):
        """Test if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_attributes_assignment(self):
        """ Test assigning values to review attributes """
        self.review.text = "Hello"
        self.review.place_id = "Lagos"
        self.review.user_id = "123"
        self.assertEqual(self.review.text, "Hello")
        self.assertEqual(self.review.place_id, "Lagos")
        self.assertEqual(self.review.user_id, "123")

    def test_place_id_default_value(self):
        """Test the default value of the 'place_id' attribute."""
        self.assertEqual(self.review.place_id, "")

    def test_user_id_default_value(self):
        """Test the default value of the 'user_id' attribute."""
        self.assertEqual(self.review.user_id, "")

    def test_text_default_value(self):
        """Test the default value of the 'text' attribute."""
        self.assertEqual(self.review.text, "")

    def test_save_method(self):
        """Test the 'save' method for updating 'updated_at'."""
        initial_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(initial_updated_at, self.review.updated_at)

    def test_to_dict_method(self):
        """Test the 'to_dict' method for generating a dictionary."""
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['id'], self.review.id)
        self.assertEqual(review_dict['created_at'],
                         self.review.created_at.isoformat())
        self.assertEqual(review_dict['updated_at'],
                         self.review.updated_at.isoformat())

    def test_str_method(self):
        """Test the '__str__' method for generating a string representation."""
        str_representation = str(self.review)
        self.assertIn(self.review.__class__.__name__, str_representation)
        self.assertIn(self.review.id, str_representation)
        self.assertIn(str(self.review.__dict__), str_representation)


if __name__ == '__main__':
    unittest.main()
