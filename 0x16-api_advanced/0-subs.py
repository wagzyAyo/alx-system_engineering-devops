#!/usr/bin/python3
"""Contains a function that get
number of subscriber for a reddit account"""
import requests


def number_of_subscribers(subreddit):
    """a function that get number of subscriber
    for a reddit account"""
    if subreddit is None or  not isinstance(subreddit, str):
        return 0
    
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    response = requests.get(url, headers=agent, allow_redirects=False)
    response = response.json()

    try:
        return response.get('data').get('subscribers')
    except Exception:
        return 0
