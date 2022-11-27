#!/usr/bin/python3
"""
Defines the city class
"""

from models.base_model import BaseModel

class City(BaseModel):
  """
  Represents the city class
  
  Attributes:
      state_id (str): The state id of the city
      name (str): The name of the city
  """
  
  state_id = ""
  name = ""
