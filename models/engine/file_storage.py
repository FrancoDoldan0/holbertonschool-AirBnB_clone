import json
import os


class FileStorage:
    def __init__(self):
        self._file_path = "file.json"
        self._objects = {}

    def all(self):
        return self._objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self._objects[key] = obj

    def save(self):
        obj_dict = {}
        for key, value in self._objects.items():
            obj_dict[key] = value.to_dict()

        with open(self._file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        if os.path.exists(self._file_path):
            with open(self._file_path, "r") as f:
                objs = json.load(f)
        if objs:

            for obj in objs.values():

                class_name = obj['__class__']

            actual_class_type = eval(class_name)

            deserialized_object = actual_class_type(**obj)

            self.new(deserialized_object)
