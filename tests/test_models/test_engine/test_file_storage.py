#!/usr/bin/python3
import unittest
import json
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        # Create an instance of FileStorage before each test
        self.storage = FileStorage()

    def tearDown(self):
        # Clean up after each test
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_empty(self):
        # Test if all() returns an empty dictionary initially
        result = self.storage.all()

        print("Actual result: ", result)
        self.assertEqual(result, {})

    def test_new(self):
        # Test if new() adds an object to __objects
        obj = BaseModel()
        self.storage.new(obj)
        result = self.storage.all()
        self.assertIn(f"BaseModel.{obj.id}", result)

    def test_save_and_reload(self):
        # Test if save() and reload() work together
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        result = self.storage.all()
        self.assertIn(f"BaseModel.{obj.id}", result)

    def test_save_with_custom_objects(self):
        # Test if save() handles custom objects correctly
        user = User()
        place = Place()
        state = State()
        city = City()
        amenity = Amenity()
        review = Review()

        self.storage.new(user)
        self.storage.new(place)
        self.storage.new(state)
        self.storage.new(city)
        self.storage.new(amenity)
        self.storage.new(review)

        self.storage.save()
        self.storage.reload()

        result = self.storage.all()
        self.assertIn(f"User.{user.id}", result)
        self.assertIn(f"Place.{place.id}", result)
        self.assertIn(f"State.{state.id}", result)
        self.assertIn(f"City.{city.id}", result)
        self.assertIn(f"Amenity.{amenity.id}", result)
        self.assertIn(f"Review.{review.id}", result)


if __name__ == '__main__':
    unittest.main()
