#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response
"""

from urllib import request, error
import sys

if __name__ == '__main__':
    try:
        req = request.Request(sys.argv[1])
        with request.urlopen(req) as resp:
            html = resp.read()
            print("{}".format(html.decode('utf-8')))

    except error.HTTPError as e:
        print("Error code: ", e.code)