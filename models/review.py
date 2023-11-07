#!/usr/bin/python3
"""
This module defines a Review class that inherits from BaseModel.

The Review class represents user reviews of places and includes
attributes for the associated place ID, user ID, and the review text.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel."""
    place_id = ""
    user_id = ""
    text = ""
