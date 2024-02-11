#!/usr/bin/python3
import unittest
import pep8
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests for the Amenity class."""

    def test_pep8_conformance_amenity(self):
        """Test PEP8 conformance for amenity.py."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

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
