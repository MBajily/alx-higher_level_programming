#!/usr/bin/python3
"""Defines a JSON reading."""
import json


def load_from_json_file(filename):
    """Create a Python object."""
    with open(filename) as f:
        # Load the json format
        return json.load(f)
