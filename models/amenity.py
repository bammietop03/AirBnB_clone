#!/usr/bin/python3
"""
This module defines an Amenity class that inherits from BaseModel.

The Amenity class represents a feature or service, and it includes
an attribute for the amenity's name.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel."""
    name = ""
