#!/usr/bin/python3
"""Use recurse to get values"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    try:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"

        headers = {'User-Agent': 'Safari/537.36'}

        params = {'limit': 25, 'after': after}

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()

            for item in data['data']['children']:
                hot_list.append(item['data']['title'])

            last_submission = data['data']['after']

            if last_submission:
                return recurse(subreddit, hot_list, after=last_submission)
            else:
                return hot_list
        else:
            return None
    except Exception as e:
        return None
