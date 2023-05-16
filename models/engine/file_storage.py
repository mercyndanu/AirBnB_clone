#!/usr/bin/python
"""
FileStorage module
"""


import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
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
        with open(self.__file_path, 'r') as f:
            obj_dict = json.load(f)
            for key, value in obj_dict.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                self.__objects[key] = obj
