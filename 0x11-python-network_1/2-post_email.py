#!/usr/bin/python3
"""2. POST an email #0
takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response
(decoded in utf-8)"""
import sys
from urllib import request, parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    params = {"email": email}
    utf_params = parse.urlencode(params).encode('utf-8')
    req = request.Request(url, data=utf_params, method='POST')
    with request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
