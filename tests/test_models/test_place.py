#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests for the Place class."""

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

    def test_review_to_dict(self):
        place = Place()
        place_dict = place.to_dict()
        expected_keys = ['__class__', 'id', 'created_at', 'updated_at']
        self.assertEqual(sorted(place_dict.keys()), sorted(expected_keys))
        self.assertEqual(place_dict['__class__'], 'Place')


if __name__ == '__main__':
    unittest.main()
