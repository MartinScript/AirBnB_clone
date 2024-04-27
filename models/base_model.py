#!/usr/bin/python3
import uuid
import datetime
import models


class BaseModel:
    """Class BaseModel"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.name = kwargs["name"]
            self.id = kwargs["id"]
            self.created_at = kwargs["created_at"]
            self.updated_at = kwargs["updated_at"]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = (
                datetime.datetime.now() if self.created_at is True else self.created_at
            )

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.created_at.isoformat()
        return new_dict
