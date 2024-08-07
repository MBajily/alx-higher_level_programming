#!/usr/bin/python3
"""a Python script that takes in a URL,
sends a request to the URL and displays
the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    u = sys.argv[1]

    response = requests.get(u)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
