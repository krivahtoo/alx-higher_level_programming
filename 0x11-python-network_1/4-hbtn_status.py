#!/usr/bin/python3
"""4. What's my status? #1
fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    data = requests.get(url).text
    res_type = type(data)
    print(f"Body response:\n\t- type: {res_type}\n\t\
- content: {data}")
