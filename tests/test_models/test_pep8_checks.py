#!/usr/bin/python3

"""Tests"""
import pep8
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review
from models.state import State
from models import __init__ as init
from models.engine import file_storage

class TestPEP8(unittest.TestCase):
    """Tests if all code complies with PEP8 standards."""

    def setUp(self):
        self.filename = None

    def test_pep8_conformance(self):
        """The test that we perform for PEP8"""
        if self.filename is not None:
            pep8style = pep8.StyleGuide(quiet=True)
            result = pep8style.check_files([self.filename])
            self.assertEqual(result.total_errors, 0, f"Found code style errors in {self.filename}.")

    def test_pep8_conformance_amenity(self):
        """Test the amenity file"""
        self.filename = 'models/amenity.py'
        self.test_pep8_conformance()

    def test_pep8_conformance_base_model(self):
        """Test the base_model file"""
        self.filename = 'models/base_model.py'
        self.test_pep8_conformance()

    def test_pep8_conformance_city(self):
        """Test the city file"""
        self.filename = 'models/city.py'
        self.test_pep8_conformance()

    def test_pep8_conformance_place(self):
        """Test the place file"""
        self.filename = 'models/place.py'
        self.test_pep8_conformance()

    def test_pep8_conformance_review(self):
        """Test the review file"""
        self.filename = 'models/review.py'
        self.test_pep8_conformance()

    def test_pep8_conformance_state(self):
        """Test the state file"""
        self.filename = 'models/state.py'
        self.test_pep8_conformance()

    def test_pep8_conformance_user(self):
        """Test the user file"""
        self.filename = 'models/user.py'
        self.test_pep8_conformance()

    def test_pep8_conformance_init(self):
        """Test the init file"""
        self.filename = 'models/__init__.py'
        self.test_pep8_conformance()

    def test_pep8_conformance_file_storage(self):
        """Test the file_storage file"""
        self.filename = 'models/engine/file_storage.py'
        self.test_pep8_conformance()

    def test_pep8_conformance_console(self):
        """Test the console file"""
        self.filename = 'console.py'
        self.test_pep8_conformance()

if __name__ == '__main__':
    unittest.main()
