"""a Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""
import sys
from urllib.request import  urlopen
import urllib.error


if __name__ == "__main__":
    try:
        with urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))

    except urllib.error.HTTPError as error:
        print('Error code:', error.code)