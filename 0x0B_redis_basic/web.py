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
    Decorator to count how many times a URL is accessed.
    """
    @wraps(method)
    def wrapper(url):
        count_key = f"count:{url}"
        redis_client.incr(count_key)
        return method(url)
    return wrapper


def cache_with_expiry(expiry=10):
    """
    Decorator to cache the result of a function with expiration time.
    """
    def decorator(method):
        @wraps(method)
        def wrapper(url):
            cache_key = f"cache:{url}"
            cached_html = redis_client.get(cache_key)
            if cached_html:
                return cached_html.decode('utf-8')

            html_content = method(url)
            redis_client.setex(cache_key, expiry, html_content)
            return html_content
        return wrapper
    return decorator

@count_url_access
@cache_with_expiry(expiry=10)
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

# Example usage
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    html_content = get_page(url)
    print(html_content)
