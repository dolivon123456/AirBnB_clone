#!/usr/bin/python3
"""Defines unittests for models/base_model.py. """
from models.base_model import BaseModel
import unittest
import datetime
import json
import os


class test_basemodel(unittest.TestCase):
    """represents test class BaseModel module """

    def __init__(self, *args, **kwargs):
        """represents test init module """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """represents test setUp module """
        pass

    def tearDown(self):
        """represents test tearDown module"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """represents test default module """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """represents test kwargs module """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """represents test kwargs_int module """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """represents test str module """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """represents test todict module """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """represents test kwargs_none module """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """represents test kwargs_one module """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """represents test id module """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """represents test created_at module """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """represents test updated_at module """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
