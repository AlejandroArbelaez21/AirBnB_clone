#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models
import copy
"""
import the modules in the code
"""


class BaseModel():
    """
    The main class
    """

    def __init__(self, *args, **kwargs):
        """ The constructor """
        if len(kwargs) > 0:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key == "created_at" or key == "updated_at":
                        timeform = "%Y-%m-%dT%H:%M:%S.%f"
                        setattr(self, key, datetime.strptime(val, timeform))
                    else:
                        setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ the __str__ display the attributes of the class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ updates the public instance attribute """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ a dictionary containing all keys/values """
        my_dict = copy.deepcopy(self.__dict__)
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
