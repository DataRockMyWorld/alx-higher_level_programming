#!/usr/bin/python3
import json

"""Module returns json representation of an object string"""


def to_json_string(my_obj):
    """Returns json representation of an object"""
    return json.dumps(my_obj)