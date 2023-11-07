#!/usr/bin/python3
"""
  This module defines a User class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""
    first_name = ""
    last_name = ""
    email = ""
    password = ""
