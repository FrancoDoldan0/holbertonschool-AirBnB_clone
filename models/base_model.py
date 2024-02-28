import uuid
from datetime import datetime

# Modelo base


class BaseModel:
    """class"""
    def __init__(self, *args, **kwargs):
        """Initializates the BaseModel instance"""
        if len(kwargs) > 0:
            for k in kwargs:
                if k is not "__class__":
                    if k is "updated_at" or k is "created_at":
                        setattr(self, k, datetime.
                                strptime(kwargs[k], "%Y-%m-%d %H:%M:%S.%f"))
                    else:
                        setattr(self, k, kwargs[k])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        ob_dict = self.__dict__.copy()
        ob_dict["__class__"] = self.__class__.__name__
        ob_dict["created_at"] = self.created_at.isoformat()
        ob_dict["updated_at"] = self.updated_at.isoformat()
        return ob_dict
