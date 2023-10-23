#!/usr/bin/python3


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as e:
        print(f"Exception: {e}")
        result = None
    return result
