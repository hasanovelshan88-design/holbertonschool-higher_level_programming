#!/usr/bin/python3
"""Module demonstrating basics of HTTP and HTTPS."""
import urllib.request


def fetch_http(url):
    """Fetch data from an HTTP URL."""
    with urllib.request.urlopen(url) as response:
        print("Status Code:", response.status)
        print("Headers:", dict(response.headers))
        print("Body:", response.read(200))


def fetch_https(url):
    """Fetch data from an HTTPS URL."""
    with urllib.request.urlopen(url) as response:
        print("Status Code:", response.status)
        print("Headers:", dict(response.headers))
        print("Body:", response.read(200))


if __name__ == "__main__":
    print("=== HTTP Request ===")
    fetch_http("http://example.com")

    print("\n=== HTTPS Request ===")
    fetch_https("https://example.com")
