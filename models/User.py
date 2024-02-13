#!/usr/bin/python3
"""
This script defines the User class, a child class of BaseModel.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user with attributes such as email, password, first name, and last name.
    """

    def __init__(self, email="", password="", first_name="", last_name=""):
        """
        Initializes a new User instance.
        """
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

