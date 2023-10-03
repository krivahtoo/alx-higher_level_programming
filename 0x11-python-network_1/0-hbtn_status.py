#!/usr/bin/python3
"""0. What's my status? #0
script that fetches https://alx-intranet.hbtn.io/status"""
from urllib import request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as res:
        data = res.read()
        parsed_data = data.decode('utf-8')
        res_type = type(data)
        print(f"Body response:\n\t- type: {res_type}\n\t\
- content: {data}\n\t- utf8 content: {parsed_data}")
