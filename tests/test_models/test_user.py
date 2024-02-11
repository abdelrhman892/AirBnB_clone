#!/usr/bin/python3
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test for the User class"""

    def test_user_instance(self):
        """Test creating an instance of the User class."""
        user = User()
        self.assertIsInstance(user, User)

    def test_user_attributes(self):
        """Test User class attributes."""
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_to_dict(self):
        user = User()
        user_dict = user.to_dict()
        expected_keys = ['__class__', 'id', 'created_at', 'updated_at']
        self.assertEqual(sorted(user_dict.keys()), sorted(expected_keys))


if __name__ == '__main__':
    unittest.main()
