#!/usr/bin/python3
"""Review class that inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Public class review"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Class State that inherits from BaseModel"""
        super().__init__(self, *args, **kwargs)
