#!/usr/bin/python3
"""queries reddit"""
import requests


def number_of_subscribers(subreddit):
    """returns subscriber count"""
    r = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit),
                      headers={"User-Agent": "anything"},
                      allow_redirects=False)
    if r.status_code == 200:
        return r.json()["data"]["subscribers"]
    return 0
