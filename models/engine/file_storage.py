#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    __filepath = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict().copy()
        with open(FileStorage.__filepath, mode="w") as file_json:
            json.dump(new_dict, file_json)

    def reload(self):
        try:
            with open(FileStorage.__filepath, mode="r") as file_json:
                new_dict = json.load(file_json)

            for key, value in new_dict.items():
                class_name = value.get("__class__")
                obj = eval(class_name + "(**value)")
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
