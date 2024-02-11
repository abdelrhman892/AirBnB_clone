#!/usr/bin/python3
import unittest
import pep8
from models.state import State


class TestState(unittest.TestCase):
    """Test the state file"""

    def test_pep8_conformance_state(self):
        """Test PEP8 conformance for state.py."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_state_instance(self):
        """Test creating an instance of the State class."""
        state = State()
        self.assertIsInstance(state, State)

    def test_state_attribute_name(self):
        """Test State class 'name' attribute."""
        state = State()
        self.assertTrue(hasattr(state, 'name'))

if __name__ == '__main__':
    unittest.main()
