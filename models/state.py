#!/usr/bin/python3
"""
This module defines a State class that inherits from BaseModel.

The State class represents a state and includes an attribute for
the state name.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel."""
    name = ""
