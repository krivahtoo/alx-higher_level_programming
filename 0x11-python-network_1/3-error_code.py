#!/usr/bin/python3
"""3. Error code #0
takes in a URL, sends a request to the URL and displays the body of
the response (decoded in utf-8)."""
import sys
from urllib import request, error

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        with request.urlopen(url) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
