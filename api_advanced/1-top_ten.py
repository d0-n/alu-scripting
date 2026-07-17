#!/usr/bin/python3
"""queries reddit"""
import requests


def top_ten(subreddit):
    """prints titles of first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10"
    r = requests.get(
        url.format(subreddit),
        headers={"User-Agent": "alu:api_advanced:v1.0"},
        allow_redirects=False
    )
    if r.status_code != 200:
        print(None)
        return
    for post in r.json()["data"]["children"]:
        print(post["data"]["title"])
