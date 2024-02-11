#!/usr/bin/python3
import unittest
import pep8
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests for the Place class."""

    def test_pep8_conformance_place(self):
        """Test PEP8 conformance for place.py."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_place_instance(self):
        """Test creating an instance of the Place class."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_attribute_city_id(self):
        """Test Place class 'city_id' attribute."""
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))

    def test_place_attribute_user_id(self):
        """Test Place class 'user_id' attribute."""
        place = Place()
        self.assertTrue(hasattr(place, 'user_id'))

    def test_place_attribute_name(self):
        """Test Place class 'name' attribute."""
        place = Place()
        self.assertTrue(hasattr(place, 'name'))

    def test_place_attribute_description(self):
        """Test Place class 'description' attribute."""
        place = Place()
        self.assertTrue(hasattr(place, 'description'))

    def test_place_attribute_number_rooms(self):
        """Test Place class 'number_rooms' attribute."""
        place = Place()
        self.assertTrue(hasattr(place, 'number_rooms'))


if __name__ == '__main__':
    unittest.main()
