#!/usr/bin/python3
"""
Sends a POST request to a given URL with a specified email.

Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    # Get the URL and email from command line arguments
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    # Create a POST request with the provided data
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        # Print the response body
        print(response.read().decode("utf-8"))
