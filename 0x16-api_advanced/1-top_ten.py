#!/usr/bin/python3
"""
1-top_ten.py
script to quesry the Reddit API and print the titles of the first 10 hot posts
listed for a given subreddit.

Usage:
    python3 1-top_ten.py <subreddit_name>

"""
import requests


def top_ten(subreddit):
    """
    top_ten(subreddit)

    Function to fetch and print the titles of the first 10 hot posts from a
    given subreddit using the Reddit API.

    Args:
        subdirect(str): The name of the subdirrect to query
    prints:
        prints the titles of the first 10 hot posts if successful.
        prints 'None' if the subreddit is invalid or if there is an erros
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) leWebKit/537.36'
            '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
    params = {
            'limit': 10
            }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        # Request was successful, parse json response
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        # request was not successfull, handle the error
        print(None)
