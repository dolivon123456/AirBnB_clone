#!/usr/bin/python3
"""BaseModel module"""

import uuid
import models
from datetime import datetime

class BaseModel():
    """BaseModel"""
    
    def __init__(self, *args, **kwargs):
        """Initialize the class instances"""
        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, DATE_TIME_FORMAT)
            
