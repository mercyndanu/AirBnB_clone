#!/usr/bin/python
"""
FileStorage module
"""


import models
import json
import os


class FileStorage:
    """
    Serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    def __init__(self):
        """
        Instantiation of attributes
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict().copy()
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r") as f:
            obj_dict = json.load(f)
            for key, obj_data in obj_dict.items():
                class_name, obj_id = key.split(".")
                module = __import__(class_name)
                class_ = getattr(module, class_name)
                obj = class_(**obj_data)
                self.__objects[key] = obj
