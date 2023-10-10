#!/usr/bin/python3
"""
a function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Get top 10 post"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {
        'User-Agent': 'Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']

            for i, post in enumerate(posts[:10], start=1):
                print(f"{i}. {post['data']['title']}")
        else:
            print(f"Failed to retrieve data for subreddit '{subreddit}': "
                  "It does not exist or has no hot posts.")
    else:
        print(f"None")
