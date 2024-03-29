#!/usr/bin/python3
"""10. Time for an interview!"""
import sys
import requests


if __name__ == "__main__":
    owner = sys.argv[1]
    repo = sys.argv[2]
    limit = 10
    url = f'https://api.github.com/repos/{repo}/{owner}/commits\
?per_page={limit}'

    response = requests.get(url).json()
    for commit in response:
        name = commit.get("commit").get("author").get("name")
        print(f'{commit.get("sha")}: {name}')
