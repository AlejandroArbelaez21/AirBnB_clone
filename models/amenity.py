#!/usr/bin/python3
"""Amenity class that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Public class Amenity"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Class Amenity that inherits from BaseModel"""
        super().__init__(self, *args, **kwargs)