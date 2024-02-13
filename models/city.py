#!/usr/bin/python3
"""
This script defines the City class, a child class of BaseModel.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city with two attributes: state ID and the name of the city.
    """

    def __init__(self, state_id="", name=""):
        """
        Initializes a new City instance.

        """
        super().__init__()
        self.state_id = state_id
        self.name = name

