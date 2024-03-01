#!/usr/bin/python3
import json
import os


class FileStorage:
    """class"""
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
        try:
            with open(self.__file_path, 'r') as file:
                loaded_data = json.load(file)
                from models.user import User
                from models.city import City
                from models.state import State
                from models.place import Place
                from models.amenity import Amenity
                from models.review import Review
                from models.base_model import BaseModel
            
                dict_classes = {
                    "Amenity": Amenity,
                    "BaseModel": BaseModel,
                    "City": City,
                    "Place": Place,
                    "Review": Review,
                    "State": State,
                    "User": User
                }
                for key, value in loaded_data.items():
                    if '__class__' in value:
                        class_name = value['__class__']
                    if class_name in dict_classes:
                        cls = dict_classes[class_name]
                        instance = cls(**value)
                        self.__objects[key] = instance
        except FileNotFoundError:
            pass
