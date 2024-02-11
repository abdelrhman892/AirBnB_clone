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
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))


if __name__ == '__main__':
    unittest.main()
