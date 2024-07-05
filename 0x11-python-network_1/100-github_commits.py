#!/usr/bin/python3
"""Time for an interview!
"""
import sys
import requests


if __name__ == "__main__":
    u = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    response = requests.get(u)
    c = response.json()

    try:
        for j in range(10):
            print("{}: {}".format(
                c[j].get("sha"),
                c[j].get("commit").get("author").get("name")))
    except IndexError:
        pass
