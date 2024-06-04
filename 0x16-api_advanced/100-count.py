#!/usr/bin/python3
""" a recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces. Javascript should count as javascript, but java should
not)
"""
import requests


def count_words(subreddit, word_list, hot_list=[], after=None, counts={}):
    """Recursively queries the Reddit API, parses the titles of hot articles,
    and counts given keywords."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyUserAgent/0.0.1'}
    params = {'after': after} if after else {}
    response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    children = data.get('data', {}).get('children', [])

    for child in children:
        title = child.get('data', {}).get('title', "").lower()
        for word in word_list:
            word_lower = word.lower()
            # Split the title into words and count exact matches
            count = sum(1 for w in title.split() if w == word_lower)
            if word_lower in counts:
                counts[word_lower] += count
            else:
                counts[word_lower] = count

    after = data.get('data', {}).get('after')
    if after is not None:
        return count_words(subreddit, word_list, hot_list, after, counts)

    # Filter out words with zero count
    counts = {word: count for word, count in counts.items() if count > 0}

    # Sort the counts dictionary by count descending then word alphabetically
    sorted_counts = sorted(
            counts.items(),
            key=lambda item: (-item[1], item[0]))

    for word, count in sorted_counts:
        print(f"{word}: {count}")

    return counts
