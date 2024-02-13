#!/usr/bin/python3
"""
This script defines the State class, a child class of BaseModel.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state with a single attribute - the name of the state.
    """

    def __init__(self, name=""):
        """
        Initializes a new State instance.
        """
        super().__init__()
        self.name = name

