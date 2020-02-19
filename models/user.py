#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Class State that inherits from BaseModel"""
        super().__init__(self, *args, **kwargs)
