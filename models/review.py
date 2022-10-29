#!/usr/bin/python3
"""Class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a Review"""
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()

        # if kwargs have values
        if len(kwargs) > 0:
            super().__init__(**kwargs)
