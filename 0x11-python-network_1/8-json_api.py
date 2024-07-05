#!/usr/bin/python3
"""a Python script that takes in a letter
and sends a POST request to
http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]

    data = {"q": letter}

    response = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        r = response.json()
        if r == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.get("id"), r.get("name")))
    except ValueError:
        print("Not a valid JSON")