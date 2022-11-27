#!/usr/bin/python3
"""Defines unittests for models/city.py. """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """represents test class city module """

    def __init__(self, *args, **kwargs):
        """represents test init module """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """represents test state_id module """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """represents test name module """
        new = self.value()
        self.assertEqual(type(new.name), str)
