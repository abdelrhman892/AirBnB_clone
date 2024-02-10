#!/usr/bin/python3
"""
Test suits for the base model
"""

import unittest
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Tests attributes of the base model
    """

    mymodel = BaseModel()

    def test_basic_attributes(self):
        """
        Tests basic imputs for the BaseModel class
        """
        self.mymodel.name = "ALX"
        self.mymodel.number = 89
        self.assertEqual([self.mymodel.name, self.mymodel.number],
                         ["ALX", 89])

    def test_datetime_format(self):
        """
        Tests for correct datetime format
        """
        created_at = self.mymodel.created_at
        updated_at = self.mymodel.updated_at

        # Check if created_at and updated_at are instances of datetime
        self.assertIsInstance(created_at, datetime)
        self.assertIsInstance(updated_at, datetime)

        # Check if created_at and updated_at are formatted
        created_at_str = created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        updated_at_str = updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')

        self.assertEqual(created_at_str, str(self.my_model.created_at))
        self.assertEqual(updated_at_str, str(self.my_model.updated_at))
    


if __name__ == '__main__':
    unittest.main()
