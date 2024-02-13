#!/usr/bin/python3
"""
This script defines the Place class, a child class of BaseModel.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a place with various attributes such as city ID, user ID, name,
    description, number of rooms, number of bathrooms, maximum guests,
    price per night, latitude, longitude, and a list of amenity IDs.
    """

    def __init__(self, city_id="", user_id="", name="", description="",
                 number_rooms=0, number_bathrooms=0, max_guest=0,
                 price_by_night=0, latitude=0.0, longitude=0.0, amenity_ids=[]):
        """
        Initializes a new Place instance.

        """
        super().__init__()
        self.city_id = city_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenity_ids = amenity_ids

