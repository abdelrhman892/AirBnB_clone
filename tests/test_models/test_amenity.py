#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests for the Amenity class."""

    def test_amenity_instance(self):
        """Test creating an instance of the Amenity class."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_amenity_attribute_name(self):
        """Test Amenity class 'name' attribute."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))

    def test_amenity_to_dict(self):
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        expected_keys = ['__class__', 'id', 'created_at', 'updated_at']
        self.assertEqual(sorted(amenity_dict.keys()), sorted(expected_keys))
        self.assertEqual(amenity_dict['__class__'], 'Amenity')


if __name__ == '__main__':
    unittest.main()
