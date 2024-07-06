#!/usr/bin/python3
"""A function that queries the Reddit API and
 returns the number of subscribers (all subscribers)"""
 
 import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns 'OK' if the subreddit has subscribers,
    or 0 if it has no subscribers or data is not found.
    """
    subreddit_URL = 'https://www.reddit.com/r/{}/about/.json'.format(subreddit)
    response = requests.get(subreddit_URL, headers={"user-agent": "user"}, allow_redirects=False)
    
    if response.status_code != 200:
        return 0
    
    subreddit_info = response.json()
    
    if "data" not in subreddit_info:
        return 0
    
    subscribers = subreddit_info["data"].get("subscribers", 0)
    
    return "OK" if subscribers > 0 else 0

# Example usage
print(number_of_subscribers("learnpython"))
