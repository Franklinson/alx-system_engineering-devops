#!/usr/bin/python3
"""
 a function that queries the Reddit API and returns the
 number of subscribers (not active users, total subscribers)
 for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Reddit API function"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {"User-Agent": "Safari/537.36"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()

            subscribers = data["data"]["subscribers"]
            return subscribers
        except (KeyError, ValueError):
            return 0
    else:
        return 0
