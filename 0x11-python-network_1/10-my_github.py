#!/usr/bin/python3
"""a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to
display your id
"""
import sys
import requests
from requests import auth


if __name__ == "__main__":
    authorize = auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=authorize)
    print(response.json().get("id"))
