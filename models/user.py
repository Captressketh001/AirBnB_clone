#!/usr/bin/python3

"""
A model that inherits from another model
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    a class User that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
