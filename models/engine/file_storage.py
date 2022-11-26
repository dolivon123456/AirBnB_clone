#!/usr/bin/python3
"""
The class FileStorage module
"""

import os.path
import json

class FileStorage:
  """ 
  serializes instances to a JSON file and
  deserializes JSON file to instances.
  """
  
  __file_path = "file.json"
  __objects = {}
  
  def all(self):
    """
    returns the dictionary __objects
    """
    return FileStorage.__objects
  
  def new(self, obj):
    """
    sets in __objects the obj with key <obj class name>.id
    """
    cls_name = type(obj).__name__
    obid = obj.id
    key = str(cls_name) + "." + str(obid)
    FileStorgae.__objects[key] = obj.to_dict()
    
  def save(self):
    """
    serializes __objects to the JSON file (path: __file_path)
    """
    js_star = json.dumps(FileStorage.__objects)
    with open(FileStorage.__file_path, 'w', encoding="UTF-8") as fd:
            fd.write(js_str)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding="UTF-8") as fd:
                js_str = fd.readline()
            FileStorage.__objects = json.loads(js_str)
