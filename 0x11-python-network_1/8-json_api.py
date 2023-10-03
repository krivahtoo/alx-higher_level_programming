#!/usr/bin/python3
"""8. Search API
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}
    res = requests.post(url, data=data)
    try:
        data = res.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
