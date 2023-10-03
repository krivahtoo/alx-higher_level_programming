#!/usr/bin/python3
"""9. My GitHub!
takes your GitHub credentials (username and password) and uses the GitHub API
to display your id"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    headers = {'Authorization': f'Bearer {password}'}
    res = requests.get("https://api.github.com/user", headers=headers)
    if (res.status_code >= 400):
        print("None")
    else:
        print(res.json()["id"])
