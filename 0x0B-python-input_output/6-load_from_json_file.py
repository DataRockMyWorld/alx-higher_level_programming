#!/usr/bin/python3
"""This module is a fxn that creates
    an object from a JSON File
"""
import json


def load_from_json_file(filename):
    """Fxn writes a python object represented by a JSON to a file"""
    with open(filename, "r", encoding="utf-8") as Myfile:
        return json.load(Myfile)
