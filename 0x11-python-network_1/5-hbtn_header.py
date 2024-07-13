#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable in the response header
"""

import sys
import requests

if __name__ == '__main__':
    resp = requests.get(sys.argv[1])
    print("{}".format(resp.headers.get('X-Request-Id')))
