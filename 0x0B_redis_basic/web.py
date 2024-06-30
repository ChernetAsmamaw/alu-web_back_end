import requests
import redis

# Initialize Redis client
redis_client = redis.Redis()

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
        # Track the number of times the URL is accessed
        count_key = f"count:{url}"
        redis_client.incr(count_key)

        # Check if the page content is cached
        cache_key = f"cache:{url}"
        cached_html = redis_client.get(cache_key)
        if cached_html:
            return cached_html.decode('utf-8')

        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()

        # Cache the page content with an expiration time of 10 seconds
        html_content = response.text
        redis_client.setex(cache_key, 10, html_content)

        return html_content

    except requests.RequestException as e:
        raise e

# Example usage
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    html_content = get_page(url)
    print(html_content)
