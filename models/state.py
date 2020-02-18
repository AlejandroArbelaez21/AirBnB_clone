#!/usr/bin/python3
"""State class that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """Public class State"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Class State that inherits from BaseModel"""
        super().__init__(self, *args, **kwargs)
