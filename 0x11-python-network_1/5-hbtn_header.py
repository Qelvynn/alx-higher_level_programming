#!/usr/bin/python3
"""
Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests

if __name__ == "__main__":
    # Get the URL from command line arguments
    url = sys.argv[1]

    # Send a GET request to the specified URL
    r = requests.get(url)

    # Print the X-Request-Id header value
    print(r.headers.get("X-Request-Id"))
