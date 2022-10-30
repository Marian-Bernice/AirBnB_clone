#!/usr/bin/python3
"""Class Amenity that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents a City"""
    name = ''

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()

        if len(kwargs) > 0:
            super().__init__(*args, **kwargs)
