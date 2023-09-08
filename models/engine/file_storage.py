#!/usr/bin/python3
"""Defines FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Class FileStorage
    Represent an abstracted storage test_engine.

    It serializes instances to a JSON file and deserializes
    JSON file to instances.

    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with the  key <obj_class_name>.id"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file __file_path."""
        object_dict = {}
        for obj in self.__objects:
            object_dict[obj] = self.__objects[obj].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(object_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        """
        try:
        with open(self.__file_path) as file:
            serialized_content = json.load(file)
            for item_id, item_data in serialized_content.items():
                class_name = item_data['__class__']
                if class_name in self.class_dict:
                    obj = self.class_dict[class_name](**item_data)
                    self.new(obj)
                else:
                    print(f"Class {class_name} not found in class_dict.")
        except FileNotFoundError:
            pass