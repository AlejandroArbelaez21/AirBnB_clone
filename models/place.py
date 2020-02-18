#!/usr/bin/python3
"""Place class that inherits from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Public class Place"""

    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ Place that inherits from BaseModel"""
        super().__init__(self, *args, **kwargs)
