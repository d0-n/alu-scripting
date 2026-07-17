#!/usr/bin/python3
"""queries reddit"""
import requests


def top_ten(subreddit):
    """prints titles of first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json"
    headers = {"User-Agent": "anything"}
    try:
        r = requests.get(
            url.format(subreddit),
            headers=headers,
            allow_redirects=False,
            params={"limit": 10}
        )
        if r.status_code != 200:
            print(None)
            return
        for post in r.json()["data"]["children"]:
            print(post["data"]["title"])
    except Exception:
        print(None)
