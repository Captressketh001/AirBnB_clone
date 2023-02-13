#!/usr/bin/python3

"""
A model state that inherits from BaseModel
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""