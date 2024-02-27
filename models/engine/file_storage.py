import uuid
from datetime import datetime

class BaseModel(self):
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now
        self.update_at = self.created_at

    def __str__(self):
        return(f"[{self.__class__.name___}] ({self.id}) {self.__dict__}")
