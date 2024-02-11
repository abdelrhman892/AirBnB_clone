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


if __name__ == '__main__':
    unittest.main()
