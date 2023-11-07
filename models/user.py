#!/usr/bin/python3
"""
This module defines a User class that inherits from BaseModel.

It includes attributes for a user's first name, last name,
email, and password.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
