#!/usr/bin/python3
"""queries reddit"""
import requests
import sys


def top_ten(subreddit):
    """prints top ten hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json"
    response = requests.get(
        url.format(subreddit),
        headers={"User-Agent": "anything"},
        allow_redirects=False
    )
    if response.status_code != 200:
        print(None)
        return
    data = response.json().get("data", {})
    for post in data.get("children", [])[:10]:
        print(post.get("data", {}).get("title"))


if __name__ == "__main__":
    top_ten(sys.argv[1])
