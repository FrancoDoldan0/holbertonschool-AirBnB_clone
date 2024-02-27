import uuid
from datetime import datetime

# Modelo base


class BaseModel:
    """class"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = self.created_at

    def __str__(self):
        return ("[{}] ([]) {}".format, (self.__class__.name___), (self.id), (self.__dict__))

    def save(self):
        self.update_at = datetime.now()

    def to_dict(self):
        ob_dict = self.__dict__.copy()
        ob_dict["__class__"] = self.__class__.__name__
        ob_dict["create_at"] = self.created_at.isoformat()
        ob_dict["update_at"] = self.update_at.isoformat()
        return ob_dict
