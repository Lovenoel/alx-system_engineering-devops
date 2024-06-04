#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit. If no results
are found for the given subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API and returns a list of titles of all
    hot articles for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyUserAgent/0.0.1'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None
    
    data = response.json()
    children = data.get('data', {}).get('children', [])
    for child in children:
        hot_list.append(child.get('data', {}).get('title'))

    after = data.get('data', {}).get('after')
    if after is not None:
        return recurse(subreddit, hot_list, after)

    return hot_list if hot_list else None
