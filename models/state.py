#!/usr/bin/python3
"""Class State"""
from models.base_model import BaseModel

class State(BaseModel):
    """Represents a state"""
    name = ''

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()

        # if kwargs have values
        if len(kwargs) > 0:
            super().__init__(**kwargs)
