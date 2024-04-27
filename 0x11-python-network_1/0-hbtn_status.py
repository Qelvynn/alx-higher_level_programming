#!/usr/bin/python3

def fetch_intranet_status():
    """
    Fetches the status from [1](https://intranet.hbtn.io/status) and displays information about the response.

    Returns:
        None
    """
    import urllib.request

    url = "https://intranet.hbtn.io/status"
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print("Body response:")
            print(f"\t- type: {type(body)}")
            print(f"\t- content: {body}")
            print(f"\t- utf8 content: {body.decode('utf-8')}")
    except urllib.error.URLError as e:
        print(f"Error fetching data from {url}: {e.reason}")

if __name__ == "__main__":
    fetch_intranet_status()
