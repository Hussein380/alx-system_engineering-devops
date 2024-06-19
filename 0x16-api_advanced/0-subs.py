#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'MyRedditScript/0.1'}
    #Make API Request
    try:
        # Make API requests
        response = requests.get(url, headers=headers)
        #check if the response status vode is 200 (ok)
        if response.status_code != 200:
            return 0
        # Parse the json response to get the number of subscribers
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except Exception as e:
        return 0


