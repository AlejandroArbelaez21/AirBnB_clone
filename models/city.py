#!/usr/bin/python3
"""City class that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Public class State"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Class City that inherits from BaseModel"""
        super().__init__(self, *args, **kwargs)
