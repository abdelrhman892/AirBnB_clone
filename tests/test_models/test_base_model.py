#!/usr/bin/python3
"""
Test suits for the base model
"""

import unittest
from datetime import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Tests attributes of the base model
    """

    def test_basic_attributes(self):
        """
        Tests basic inputs for the BaseModel class
        """
        obj = BaseModel()
        obj.name = "ALX"
        obj.number = 89
        self.assertEqual([obj.name, obj.number],
                         ["ALX", 89])

    def test___init___with_arguments(self):
        kwargs = {
            'created_at': '2024-02-10T12:00:00.000000',
            'updated_at': '2024-02-10T12:00:00.000000',
            'name': 'Test Name',
        }
        obj = BaseModel(**kwargs)
        self.assertEqual(obj.created_at, datetime(2024, 2, 10, 12, 0))
        self.assertEqual(obj.updated_at, datetime(2024, 2, 10, 12, 0))
        self.assertEqual(obj.name, 'Test Name')

    def test___init___without_arguments(self):
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test___init___without_arguments_values(self):
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test___init___with_invalid_datetime_format(self):
        kwargs = {
            'created_at': 'invalid_datetime_format',
            'updated_at': 'invalid_datetime_format',
            '__class__': 'TestInvalidFormat'
        }
        with self.assertRaises(ValueError):
            BaseModel(**kwargs)

    def test___str___method(self):
        obj = BaseModel()
        expected_output = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected_output)

    def test_save(self):
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save()
        updated_updated_at = obj.updated_at
        self.assertNotEqual(initial_updated_at, updated_updated_at)
        self.assertTrue(updated_updated_at > initial_updated_at)

    def test_to_dict_method(self):
        # Test the to_dict method
        obj = BaseModel()
        obj_dict = obj.to_dict()

        # Check if '__class__', 'created_at', 'updated_at', and 'id' keys exist
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('id', obj_dict)

        # Check if values are formatted correctly
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'],
                         obj.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(obj_dict['updated_at'],
                         obj.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f'))


if __name__ == '__main__':
    unittest.main()
