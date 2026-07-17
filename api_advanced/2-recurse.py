#!/usr/bin/python3
"""queries reddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns list of all hot article titles recursively"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=100"
    url = url.format(subreddit)
    if after:
        url += "&after={}".format(after)
    r = requests.get(
        url,
        headers={"User-Agent": "anything"},
        allow_redirects=False
    )
    if r.status_code != 200:
        return None
    data = r.json()["data"]
    for post in data["children"]:
        hot_list.append(post["data"]["title"])
    if data["after"]:
        return recurse(subreddit, hot_list, data["after"])
    return hot_list
