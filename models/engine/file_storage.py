#!/usr/bin/python3
"""
file storage file containing FileStorage class
"""


class FileStorage():
    """
    serialized instances to JSON and deserializes JSON files
    """
    __file_path = []
    __objects = {}

    def all(self):
        """returns the dictionary objects"""
        return __objects

    def new(self, obj):
        """sets in objects obj with the key in obj class id"""
        __objects[obj.__class__.__name__.id] = obj

    def save(self):
        """serializes objects to json file"""
        for key, value in __objects.items():
#            value =
            with open(__objects + ".json", 'w', encoding='utf-8') as file:
                file.write(json.dumps)

    def reload(self):
        """deserialized the json file to objects only if json file exist"""
