#!/usr/bin/python3
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        for key, value in self.__objects.items():
            if key == (obj.__class__.__name__, obj.id):
                self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, "w") as jsonFile:
            json.dump(self.__objects, jsonFile)

    def reload(self):
        if self.__file_path != "":
            with open(self.__file_path, "r") as jsonFile:
                self.__objects = json.load(jsonFile)
