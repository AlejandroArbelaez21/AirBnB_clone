#!/usr/bin/python3
from _datetime import datetime
import uuid
    """
    import the modules in the code
    """

class BaseModelque:
    """
    The main class
    """
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        print ("[<{}>] (<{}>) <{}>".format(self.id, self.__dict__)

    def save(self):
