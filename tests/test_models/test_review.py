#!/usr/bin/python3
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests for the Review class."""

    def test_review_instance(self):
        """Test creating an instance of the Review class."""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_attribute_place_id(self):
        """Test Review class 'place_id' attribute."""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))

    def test_review_attribute_user_id(self):
        """Test Review class 'user_id' attribute."""
        review = Review()
        self.assertTrue(hasattr(review, 'user_id'))

    def test_review_attribute_text(self):
        """Test Review class 'text' attribute."""
        review = Review()
        self.assertTrue(hasattr(review, 'text'))

if __name__ == '__main__':
    unittest.main()
