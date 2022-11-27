#!/usr/bin/python3
"""Defines unittests for models/place.py. """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """represents test class place module """

    def __init__(self, *args, **kwargs):
        """represents test init module """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """represents test city module """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """represents test user module """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """represents test name module """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """represents test description module """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """represents test number_rooms module """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """represents test number_bathroom module """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """represents test max_guest module """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """represents test price_by_night module """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """represents test latitude module """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """represents test longitude module """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """represents test amenity module """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
