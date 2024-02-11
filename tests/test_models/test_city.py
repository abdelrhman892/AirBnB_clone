#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Tests for the City class."""

    def test_city_instance(self):
        """Test creating an instance of the City class."""
        city = City()
        self.assertIsInstance(city, City)

    def test_city_attribute_state_id(self):
        """Test City class 'state_id' attribute."""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))

    def test_city_to_dict(self):
        city = City()
        city_dict = city.to_dict()
        expected_keys = ['__class__', 'id', 'created_at', 'updated_at']
        self.assertEqual(sorted(city_dict.keys()), sorted(expected_keys))
        self.assertEqual(city_dict['__class__'], 'City')


if __name__ == '__main__':
    unittest.main()
