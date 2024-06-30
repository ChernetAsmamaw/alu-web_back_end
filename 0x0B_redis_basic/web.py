#!/usr/bin/env python3
'''
Implementing an expiring web cache and tracker
'''

import requests
import redis
from functools import wraps

# Initialize Redis client
redis_client = redis.Redis()

def count_url_access(method):
    """
    Decorator to count how many times a URL is accessed and cache its content with expiry.
    """
    @wraps(method)
    def wrapper(url):
        cached_key = "cached:" + url
        cached_data = redis_client.get(cached_key)
        if cached_data:
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        html_content = method(url)

        redis_client.incr(count_key)
        redis_client.setex(cached_key, 10, html_content)  # Cache expires in 10 seconds
        return html_content
    return wrapper

@count_url_access
def get_page(url: str) -> str:
    '''
    Fetches the HTML content of a given URL using the requests module.

    Args:
        url (str): The URL of the webpage to fetch.

    Returns:
        str: The HTML content of the webpage.

    Raises:
        requests.RequestException: If there was an error fetching the webpage.
    '''
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        raise e
