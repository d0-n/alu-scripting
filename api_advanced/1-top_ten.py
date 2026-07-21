#!/usr/bin/python3
"""queries reddit"""
import sys

import requests


def top_ten(subreddit):
    """prints top ten hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json"
    headers = {"User-Agent": "linux:alu_api:v1.0.0"}
    r = requests.get(url.format(subreddit),
                     headers=headers,
                     allow_redirects=False)
    if r.status_code != 200:
        print(None)
        return
    data = r.json().get("data", {})
    children = data.get("children", [])
    for i in range(min(10, len(children))):
        print(children[i].get("data", {}).get("title"))


if __name__ == "__main__":
    top_ten(sys.argv[1])
