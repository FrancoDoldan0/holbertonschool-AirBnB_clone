#!/usr/bin/python3
"""filestorage class"""
import json
from models.base_model import BaseModel


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
        """reload"""
        defclass = {
            'BaseModel': BaseModel
        }

        try:
            with open(FileStorage.__file_path, "r") as file:
                deserialized = json.load(file)
                for key, value in deserialized.items():
                    classname = value["__class__"]
                    if classname in defclass:
                        newobj = defclass[classname](**value)
                        key = "{}.{}".format(classname, newobj.id)
                        FileStorage.__objects[key] = newobj
        except FileNotFoundError:
            pass
