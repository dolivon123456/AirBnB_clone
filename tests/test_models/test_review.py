#!/usr/bin/python3
""" Test module for the class review"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ test module for review"""

    def __init__(self, *args, **kwargs):
        """represents test init module """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """represents test place module """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """represents test user module """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """represents test text module """
        new = self.value()
        self.assertEqual(type(new.text), str)
