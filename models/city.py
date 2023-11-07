#!/usr/bin/python3
"""
This module defines a City class thati inherits from BaseModel.

The City class represents a city and includes attributes for
the state ID and the city name.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City  class that inherits from BaseModel"""
    state_id = ""
    name = ""
