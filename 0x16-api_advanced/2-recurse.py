#!/usr/bin/python3
"""
2-recurse.py

Recursive function to query the Reddit API and
return a list containing the titles
of all hot articles for a given subreddit.

Prototype:
    def recurse(subreddit, hot_list=[])

"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    recurse(subreddit, hot_list=[], after=None)

    Recursive function to fetch all hot posts from a given
    subreddit using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list, optional): List to accumulate titles of hot posts.
        Defaults to [].
        after (str, optional): Parameter for pagination in Reddit API.
        Defaults to None.

    Returns:
        list or None: List containing titles of all hot posts if
        successful, or None if the
                      subreddit is invalid or no results are found.
    """
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    params = {
        'limit': 100
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        after = data['data']['after']

        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        # Recursively fetch next page if 'after' token is present
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        print(f"Request failed for subreddit: {subreddit}. status code: {response.status_code}")
        return None
