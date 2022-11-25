#!/usr/bin/python3
"""
BaseModel module
"""

import uuid
import models
from json import JSONEncoder
from datetime import datetime

class BaseModel():
    """BaseModel class"""
    
    def __init__(self, *args, **kwargs):
        """Initialize the class instances"""
        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(
                            value, 
                            DATE_TIME_FORMAT)
                elif key == "__class__":
                    continue
            
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            
def __str__(self):
    """Returns a formatted string"""
    return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

def save(self):
    """updates the public instance attribute"""
    self.updated_at = datetime.now()
    models.storage.save()
    
def to_dict(self):
    """ returns a dictionary containing all keys/values"""
    new_dict = self.__dict__.copy()
    new_dict['created_at] = new_dict['created_at].isoformat()
    new_dict['updated_at] = new_dict['updated_at].isoformat()
    new_dict['__class__'] = self.__class__.__name__
    return new_dict


class BaseModelEncoder(JSONEncoder):
    """
    JSONEncoder for base model
    """
    def default(self, o):
        """default module"""
        if isinstance(o, BaseModule):
            return o.to_dict()
        return supper().default(o)
