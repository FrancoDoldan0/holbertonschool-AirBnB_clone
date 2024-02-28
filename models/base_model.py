import uuid
from datetime import datetime

# Modelo base


class BaseModel:
    def _init_(self, *args, **kwargs):
        """BaseModel"""
        if len(kwargs) > 0:
            for k in kwargs:
                if k is not "_class_":
                    if k is "updated_at" or k is "created_at":
                        setattr(self, k, datetime.
                                strptime(kwargs[k], "%Y-%m-%d %H:%M:%S.%f"))
                    else:
                        setattr(self, k, kwargs[k])
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
