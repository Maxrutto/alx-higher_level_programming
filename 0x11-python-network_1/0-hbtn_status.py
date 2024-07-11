#!/usr/bin/python3

"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        html_output = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(html_output)))
        print("\t- content: {}".format(html_output))
        print("\t- utf8 content: {}".format(html_output.decode('utf-8')))
