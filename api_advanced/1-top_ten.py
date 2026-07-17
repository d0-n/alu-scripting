#!/usr/bin/python3
"""queries reddit"""
import requests


def top_ten(subreddit):
    """prints top ten hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json"
    r = requests.get(
        url.format(subreddit),
        headers={"User-Agent": "anything"},
        allow_redirects=False,
        params={"limit": 10}
    )
    if r.status_code == 200:
        for post in r.json()["data"]["children"]:
            print(post["data"]["title"])
    else:
        print("None")
