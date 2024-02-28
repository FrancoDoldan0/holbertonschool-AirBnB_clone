import uuid
from datetime import datetime

# Modelo base


class BaseModel:
    def __init__(self, *args, **kwargs):
        """BaseModel"""
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.now())
                if k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def to_dict(self):
        ob_dict = self.__dict__.copy()
        ob_dict["__class__"] = self.__class__.__name__
        ob_dict["created_at"] = self.created_at.isoformat()
        ob_dict["updated_at"] = self.updated_at.isoformat()
        return ob_dict
