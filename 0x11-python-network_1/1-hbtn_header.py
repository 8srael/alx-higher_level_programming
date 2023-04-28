#!/usr/bin/python3

""" Script that
- takes a URL in arg
- sends a request to the URL
- displays the value of the X-Request-Id variable
found in the header of the response
- uses urllib and sys packages
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        headers = response.info()
        print(headers['X-Request-Id'])
