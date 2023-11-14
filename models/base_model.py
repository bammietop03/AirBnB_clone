#!/usr/bin/python3
"""
This module defines a BaseModel class that defines all common
attributes/methods for other classes
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Represents a base model for an object with common attributes and methods.

    Attributes:
        id (str): A unique identifier for the object.
        created_at (datetime): The date and time the object was created.
        updated_at (datetime): The date and time the object was last updated.

    Methods:
        __init__(**kwargs):
            Initializes a BaseModel instance with provided keyword arguments.

        __str__():
            Returns a string representation of the object, including class
            name, id, and attributes.

        save():
            Updates the 'updated_at' attribute to the current date and time.

        to_dict():
            Returns a dictionary representation of the object's attributes.
            Includes 'created_at' and 'updated_at' as ISO formatted strings.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance.

        Args:
            **kwargs: Keyword arguments to set object attributes.

        If kwargs is not empty, it sets object attributes based on key-value
        pairs in kwargs. Converts 'created_at' and 'updated_at' strings to
        datetime objects. If kwargs is empty, it generates a new id and
        timestamps.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Returns:
            str: A string representation of the object in the format
            "[Class Name] (id) {attributes}".
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute to the current date and time.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns:
            dict: A dictionary containing the object's attributes.
            'created_at' and 'updated_at' are included as ISO formatted
            strings.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    @classmethod
    def get_subclasses(cls):
        subclasses = [cls]
        for subclass in cls.__subclasses__():
            subclasses.append(subclass)
        return subclasses
