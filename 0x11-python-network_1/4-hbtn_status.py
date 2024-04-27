#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status.
"""
import requests

if __name__ == "__main__":
    # Send a GET request to the specified URL
    r = requests.get("https://intranet.hbtn.io/status")

    # Print the response body information
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
