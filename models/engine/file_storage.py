#!/usr/bin/python3
"""
A class FileStorage that serializes instances to a JSON file and
deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Handles the serialization and deserialization of objects to and
    from a JSON file.

    Attributes:
        __file_path (str): The path to the JSON file used for storage.
        __objects (dict): A dictionary that stores objects by <class
                          name>.id.

    Public Methods:
        all(self): Returns a dictionary of all stored objects.
        new(self, obj): Adds an object to the storage dictionary.
        save(self): Serializes and saves the storage dictionary to the
                    JSON file.
        reload(self): Deserializes and loads objects from the JSON file
                      (if it exists).

    Usage:
        To store and manage objects persistently, create an instance of
        FileStorage. Use the public methods to interact with the stored
        objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized = {key: obj.to_dict() for key, obj in
                      self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists). If the file doesn’t exist, no exception should
        be raised.
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    obj = eval(value['__class__'])(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
