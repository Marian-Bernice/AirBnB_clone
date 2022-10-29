#!/usr/bin/python3
"""Class City"""
from models.base_model import BaseModel

class City(BaseModel):
    """Represents a City"""
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()

        # if kwargs have values
        if len(kwargs) > 0:
            super().__init__(**kwargs)
