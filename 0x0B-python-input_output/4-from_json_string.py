#!/usr/bin/python3
"""Returns a python data structure representing a JSON string"""
import json


def from_json_string(my_str):
    """Fxn returns a python object represented by a JSON string"""
    return json.loads(my_str)
