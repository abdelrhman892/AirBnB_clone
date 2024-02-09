#!/usr/bin/python3
import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}_{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        from models.base_model import BaseModel
        objects_to_serialize = {}
        for key, value in self.__objects.items():
            if isinstance(value, BaseModel):
                objects_to_serialize[key] = value.to_dict()
            else:
                objects_to_serialize[key] = value
        with open(self.__file_path, "w") as jsonFile:
            json.dump(objects_to_serialize, jsonFile)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as jsonFile:
                self.__objects = json.load(jsonFile)
