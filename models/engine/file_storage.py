#!/usr/bin/python3
"""filestorage class"""
import json
from models.base_model import BaseModel
import os


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
        with open(FileStorage.__file_path, 'w') as f:
            data = {}

            for key, value in FileStorage.__objects.items():
                dict_object = value.to_dict()

                data[key] = data

            json.dump(data, f)

        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)

            for key, value in obj_dict.items():
                class_name, obj_id = key.split(".")
                obj = globals()[class_name](**value)
                self.__objects[key] = obj

        except FileNotFoundError:
            pass
