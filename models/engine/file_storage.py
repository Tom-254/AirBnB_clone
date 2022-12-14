#!/usr/bin/python3
"""
Module serializes instances to a JSON file and
deserializes JSON file to instances
"""
import json

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    serializes instances to a JSON
    file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with
        key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)

        self.__objects[key] = obj

    def save(self):
        """
            serializes __objects to the JSON file
            (path: __file_path)
        """
        tmp_dict = {}
        for key, value in self.__objects.items():
            tmp_dict[key] = value.to_dict()

        with open(self.__file_path, "w") as write_file:
            json.dump(tmp_dict, write_file)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """
        defined_classes = {
            "User": User,
            "BaseModel": BaseModel,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }
        try:
            temp_dict = {}
            with open(self.__file_path, "r") as read_file:
                realoded_dict = json.load(read_file)
            for key, value in realoded_dict.items():
                if value['__class__'] in defined_classes:
                    temp_dict[key] = defined_classes[value['__class__']](**value)
            self.__objects = temp_dict

        except Exception as ex:
            pass
