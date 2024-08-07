#!/usr/bin/python3

"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as
a parameter, and displays the body of the response
"""

import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    email = urllib.parse.urlencode({'email': sys.argv[2]}).encode('ascii')
    req = urllib.request.Request(sys.argv[1], email)
    with urllib.request.urlopen(req) as resp:
        html = resp.read()
        print("{}".format(html.decode('utf-8')))
