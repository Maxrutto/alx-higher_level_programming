#!/usr/bin/python3
"""
Python script that list 10 commits (from the most recent to
oldest) of the repository “rails” by the user “rails”
"""

import requests
import sys

if __name__ == '__main__':
    base_url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2], sys.argv[1])

    r = requests.get(base_url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
