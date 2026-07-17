#!/usr/bin/python3
"""queries reddit"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """prints sorted count of keywords in hot article titles recursively"""
    if counts is None:
        counts = {}
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if after:
        url += "&after={}".format(after)
    r = requests.get(url,
                      headers={"User-Agent": "anything"},
                      allow_redirects=False)
    if r.status_code != 200:
        return
    data = r.json()["data"]
    for post in data["children"]:
        title_words = post["data"]["title"].lower().split()
        for word in word_list:
            w = word.lower()
            counts[w] = counts.get(w, 0) + title_words.count(w)
    if data["after"]:
        count_words(subreddit, word_list, data["after"], counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))
