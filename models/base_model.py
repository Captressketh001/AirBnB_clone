#!/usr/bin/python3
import uuid
from datetime import datetime
import models

"""
Parent class to all other classes in this project
"""

class BaseModel():
    """
    defines all common attributes/methods for other classes
    Public Instance Attributes:
        id:  string - assign with an uuid when an instance is created
        created_at: datetime - assign with the current datetime when an instance is created
        updated_at: datetime - assign with the current datetime when an instance is created 
        and it will be updated every time you change your object
    Public Instance Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __repr__(self)
        __save__(self)
        to_dict(self)
    """
    def __init__(self, *args, **kwargs):
        """
        Public instance attribute (id, created_at, updated_at) 
        assigned when an instance is created
        """
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"], date_format)
                elif "updated_at":
                    self.updated_at = datetime.strptime(kwargs["updated_at"], date_format)
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, value)
        else:
            """
            New instance
            """
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            """
            if it’s a new instance (not from a dictionary representation), 
            add a call to the method new(self) on storage
            """
            models.storage.new(self)

    def __str__(self):
        """
        Prints the class name, id and dict
        """
        return ('[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        """
        returns string repr
        """
        return (self.__str__())

    def save(self):
        """"
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

        """
        link BaseModel to FileStorage by using the variable storage
        """
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result
    
