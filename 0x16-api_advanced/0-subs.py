#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
     Queries the Reddit API and returns the number of subscribers for a given subreddit.
     If an invalid subreddit is given, returns 0.
        :param subreddit: Subreddit name to query.
        :return: Number of subscribers, or 0 if subreddit is invalid.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'MyRedditScript/0.1'}
    #Make API Request
    try:
        # Make API requests
        response = requests.get(url, headers=headers, allow_redirects=False)
        #check if the response status vode is 200 (ok)
        if response.status_code != 200:
            return 0
        # Parse the json response to get the number of subscribers
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except requests.RequestException:
        return 0


