#!/usr/bin/python3
"""Defines unittests for models/amenity.py. """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """represents test amenity class module """

    def __init__(self, *args, **kwargs):
        """represents test init module """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """represents test name module """
        new = self.value()
        self.assertEqual(type(new.name), str)
