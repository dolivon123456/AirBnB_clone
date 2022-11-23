#!/usr/bin/python3
"""Defining the HBNB console"""

import cmd
import models

class HBNBCommand(cmd.Cmd):
  """cmd clone"""
  intro = "Welcome to the AirBnB console."
  prompt = "(hbnb)"
