import json

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
        try:
            with open(self._file_path, "r") as file:
                obj_dict = json.load(file)

            for key, value in obj_dict.items():
                class_name, obj_id = key.split(".")
                obj = globals()[class_name](**value)
                self._objects[key] = obj

        except FileNotFoundError:
            pass
