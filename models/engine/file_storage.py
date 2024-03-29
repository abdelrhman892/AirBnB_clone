#!/usr/bin/python3
import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        if not self.__objects:
            return {}
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        objects_to_serialize = {}
        for key, value in self.__objects.items():
            if (isinstance(value, BaseModel) or
                    isinstance(value, User) or
                    isinstance(value, Place) or
                    isinstance(value, State) or
                    isinstance(value, City) or
                    isinstance(value, Amenity) or
                    isinstance(value, Review)):
                objects_to_serialize[key] = value.to_dict()
            else:
                objects_to_serialize[key] = value
        with open(self.__file_path, "w") as jsonFile:
            json.dump(objects_to_serialize, jsonFile)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_name = class_name.lower()  # Convert to lowercase
                    module_name = 'models.base_model'
                    module = __import__(module_name, fromlist=[class_name])
                    cls = getattr(module, 'BaseModel')
                    self.__objects[key] = cls(**value)
