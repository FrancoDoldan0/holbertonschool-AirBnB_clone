import json
from models.base_model import BaseModel
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
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                objs = json.load(f)
        else:
            objs = {}

        if objs:
            for obj in objs.values():
                class_name = obj['__class__']
                actual_class_type = eval(class_name)
                deserialized_object = actual_class_type(**obj)
                self.new(deserialized_object)
