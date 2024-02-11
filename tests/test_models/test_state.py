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
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertEqual(state.name, "")

    def test_state_to_dict(self):
        state = State()
        state_dict = state.to_dict()
        expected_keys = ['__class__', 'id', 'created_at', 'updated_at']
        self.assertEqual(sorted(state_dict.keys()), sorted(expected_keys))


if __name__ == '__main__':
    unittest.main()
