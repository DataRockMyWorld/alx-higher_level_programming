#!/usr/bin/python3
"""This module writes an object to text file
using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Fxn writes a python object represented by a JSON to a file"""
    with open(filename, "w", encoding="utf-8") as Myfile:
        return json.dump(my_obj, Myfile)
