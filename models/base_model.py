#!/usr/bin/python3
from _datetime import datetime
from uuid import uuid4
from models import storage
from models.engine.file_storage import FileStorage
"""
import the modules in the code
"""


class BaseModel:
    """
    The main class
    """
    id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """ The constructor """
        if kwargs is not None:
            for key, value in kwargs.items():
                if key is not '__class__':
                    if key == 'created_at':
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    if key == 'updated_at':
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.updated_at = datetime.now()
            self.id = str(uuid4())
            self.created_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ the __str__ display the attributes of the class"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """ updates the public instance attribute """
        self.updated_at = datetime.now()
        storage.save()



    def to_dict(self):
        """ a dictionary containing all keys/values """
        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict

