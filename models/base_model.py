import uuid
from datetime import datetime

# Modelo base


class BaseModel:
    """class"""
    def _init_(self):
        """base"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        ob_dict = self.__dict__.copy()
        ob_dict["_class"] = self.__class__.__name__
        ob_dict["created_at"] = self.created_at.isoformat()
        ob_dict["updated_at"] = self.updated_at.isoformat()
        return ob_dict
