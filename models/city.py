#!/usr/bin/python3

"""
A model state that inherits from BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    Inherits from BaseModel
    """
    state_id = ""
    name = ""
