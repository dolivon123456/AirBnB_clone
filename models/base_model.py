#!/usr/bin/python3
"""
BaseModel module
"""

from uuid import uuid4
import models
from datetime import datetime

class BaseModel():
    """
    BaseModel class
    """
    
    def __init__(self, *args, **kwargs):
        """
        Initialize the class instances
        """
        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, DATE_TIME_FORMAT)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)
            
    def __str__(self):
         """
         Returns a formatted string
         """
            clname = self.__class__.__name__
            return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
     
    def save(self):
        """
        updates the public instance attribute
        """
        self.updated_at = datetime.now()
        models.storage.save()
    
    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        """
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
