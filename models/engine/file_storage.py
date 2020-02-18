#!/usr/bin/python3
import json
from models.base_model import BaseModel
import os
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

"""
file storage file containing FileStorage class
"""

dict_class = {'BaseModel': BaseModel, 'User': User, 'Amenity': Amenity,
              'City': City, 'Place': Place, 'Review': Review, 'State': State}


class FileStorage():
    """
    serialized instances to JSON and deserializes JSON files
    """
#    dir_parent = os.getcwd()
#    __file_path = dir_parent + 'file.json'
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """sets in objects obj with the key in obj class id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes objects to json file"""
        new = {}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            for key, value in self.__objects.items():
                new[key] = value.to_dict()
            text = json.dumps(new)
            file.write(text)

    def reload(self):
        """deserialized the json file to objects only if json file exist"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                new_dict = json.loads(file.read())
            for key, value in new_dict.items():
                self.__objects[key] = dict_class[value['__class__']](**value)
        except IOError:
            pass
