#!/usr/bin/python3
"""filestorage class"""
import json
from os import path


class FileStorage:
    """ class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.state import State

        if path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                for value in json.loads(file.read()).values():
                    eval(value["__class__"])(**value)
