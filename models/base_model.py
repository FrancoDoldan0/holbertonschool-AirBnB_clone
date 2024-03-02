#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4


# Modelo base
class BaseModel:
    def __init__(self, *args, **kwargs):
        from models import storage
        """
        if kwargs arguments are provided. initializes the object's attributes,
        excluding special keys like __class__ and work whit time_keys.
        If there are no kwargs, it generates a new id, sets current timestamps,
        and adds the object to storage.
        """
        if kwargs:
            excluded_keys = ['__class__']
            time_keys = ['created_at', 'updated_at']

            for key, value in kwargs.items():
                if key in excluded_keys:
                    continue
                elif key in time_keys:
                    tm_obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, tm_obj)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            current_time = datetime.now()
            self.created_at = current_time
            self.updated_at = current_time
            storage.new(self)

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        ob_dict = self.__dict__.copy()
        ob_dict["__class__"] = self.__class__.__name__
        ob_dict["created_at"] = self.created_at.isoformat()
        ob_dict["updated_at"] = self.updated_at.isoformat()
        return ob_dict
