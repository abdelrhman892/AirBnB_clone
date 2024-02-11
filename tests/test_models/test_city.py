#!/usr/bin/python3
import unittest
import pep8
from models.city import City


class TestCity(unittest.TestCase):
    """Tests for the City class."""

    def test_pep8_conformance_city(self):
        """Test PEP8 conformance for city.py."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_city_instance(self):
        """Test creating an instance of the City class."""
        city = City()
        self.assertIsInstance(city, City)

    def test_city_attribute_state_id(self):
        """Test City class 'state_id' attribute."""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))


if __name__ == '__main__':
    unittest.main()
