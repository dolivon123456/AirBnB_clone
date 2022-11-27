#!/usr/bin/python3
"""Defines unittests for models/user.py. """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """represents test user module """

    def __init__(self, *args, **kwargs):
        """represents test init module """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """represents test first_name module """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """represents test last_name module """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """represents test email module """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """represents test password module"""
        new = self.value()
        self.assertEqual(type(new.password), str)
