#!/usr/bin/env python3
"""
Cache web module
"""

import redis
import requests
from typing import Callable
from functools import wraps

# Initialize Redis client
redis_client = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """
    Decorator to count how many times a URL is accessed and cache its content with expiry.

    Args:
        method (Callable): The function to decorate.

    Returns:
        Callable: The decorated function.
    """

    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Wrapper function that counts URL accesses and caches content.

        Args:
            url (str): The URL to fetch.

        Returns:
            str: The HTML content of the webpage.
        """
        redis_client.incr(f"count:{url}")
        cached_html = redis_client.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')

        html_content = method(url)
        redis_client.setex(f"cached:{url}", 10, html_content)  # Cache expires in 10 seconds
        return html_content

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a given URL using the requests module.

    Args:
        url (str): The URL of the webpage to fetch.

    Returns:
        str: The HTML content of the webpage.

    Raises:
        requests.RequestException: If there was an error fetching the webpage.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        raise e
