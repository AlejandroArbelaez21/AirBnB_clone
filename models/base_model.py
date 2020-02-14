#!/usr/bin/python3
import datetime
from uuid import uuid4
"""
import the modules in the code
"""


class BaseModel:
    """
    The main class
    """
    def __init__(self, id=None, created_at=None, update_at=None):
        """ The constructor """
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ the __str__ display the attributes of the class"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """ updates the public instance attribute """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ a dictionary containing all keys/values """
        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        return my_dict
