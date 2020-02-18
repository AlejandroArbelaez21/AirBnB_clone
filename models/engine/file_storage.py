#!/usr/bin/python3
#from models import storage
import json

"""
file storage file containing FileStorage class
"""


class FileStorage():
    """
    serialized instances to JSON and deserializes JSON files
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """sets in objects obj with the key in obj class id"""
        key = self.obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes objects to json file"""
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            new = {}
            for key, value in self.__objects.items():
                new[key] = value.to_dict()
            text = json.dumps(new)
            file.write(text)

    def reload(self):
        """deserialized the json file to objects only if json file exist"""
        with open(self.__file_path, 'r', encoding='utf-8') as file:
            try:
                new_dict = {}
                new_dict = json.loads(file.read())
                for key, value in new_dict.items():
                    self.__objects[key] = models.Class
            except IOError:
                return
