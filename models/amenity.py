#!/usr/bin/python3
"""
Defines the Amenity class, a child class of BaseModel.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity with a single attribute: name (initialized as an empty string)."""
    name = ""

