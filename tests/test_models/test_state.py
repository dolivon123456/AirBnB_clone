#!/usr/bin/python3
"""Test for the class state """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ represents test state module"""

    def __init__(self, *args, **kwargs):
        """represents test init module """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """represents test name module """
        new = self.value()
        self.assertEqual(type(new.name), str)
