#!/usr/bin/env python3
"""This module defines unittests for the BaseModel"""
import unittest
from unittest import mock
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """The defined class with different cases to test BaseModel class"""
    def test_base_model_creation(self):
        """Test creating a BaseModel instance"""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_base_model_init_with_kwargs(self):
        """Test creating a BaseModel instance with keyword arguments"""
        data = {
            'id': 'test_id',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        obj = BaseModel(**data)
        self.assertEqual(obj.id, 'test_id')
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_base_model_str_representation(self):
        """Test the __str__ method of BaseModel"""
        obj = BaseModel()
        obj_str = str(obj)
        self.assertIn('BaseModel', obj_str)
        self.assertIn(obj.id, obj_str)

    def test_base_model_save(self):
        """Test the save method of BaseModel"""
        obj = BaseModel()
        original_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, original_updated_at)

    def test_base_model_to_dict(self):
        """Test the to_dict method of BaseModel"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_base_model_id_generation(self):
        """Test that unique IDs are generated for BaseModel instances"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_base_model_created_at(self):
        """Test that 'created_at' is a valid datetime object"""
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)

    def test_base_model_updated_at(self):
        """Test that 'updated_at' is updated when calling save()"""
        obj = BaseModel()
        original_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, original_updated_at)

    def test_base_model_to_dict_format(self):
        """Test the format of the dictionary returned by to_dict()"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_datetime_attributes(self):
        """Test the 'created_at' and 'updated_at' attributes are datetime
        objects"""
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_datetime_attributes_have_microsecond_precision(self):
        """Test microsecond precision of the `updated_at` attribute in a
        BaseModel instance."""
        obj = BaseModel()
        self.assertGreaterEqual(
            obj.updated_at.microsecond, 0
        )
        self.assertLessEqual(
            obj.updated_at.microsecond, 999999
        )

    def test_str(self):
        """Test the string representation of the object"""
        obj = BaseModel()
        obj_str = str(obj)
        self.assertIn('BaseModel', obj_str)
        self.assertIn(obj.id, obj_str)

    def test_base_model_save(self):
        """Test the save method of BaseModel"""
        obj = BaseModel()
        original_updated_at = obj.updated_at
        save_output = obj.save()
        self.assertNotEqual(obj.updated_at, original_updated_at)
        self.assertIsNone(save_output)

    @mock.patch.object(storage, 'save')
    def test_save_calls_storage_save(self, mocked_save):
        obj = BaseModel()
        obj.save()
        mocked_save.assert_called_once()


if __name__ == '__main__':
    unittest.main()
