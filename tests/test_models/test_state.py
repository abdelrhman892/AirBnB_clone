#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test the state file"""

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
