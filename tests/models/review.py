#!/usr/bin/python3
"""Module for Review classinherited from basemodel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Implimenting class representing a Review."""
    place_id = ""
    user_id = ""
    text = ""
