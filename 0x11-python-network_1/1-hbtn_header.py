#!/usr/bin/python3

def fetch_x_request_id(url):
    """
    Fetches the X-Request-Id header variable from a given URL and displays it.

    Args:
        url (str): The URL to fetch the header from.

    Returns:
        None
    """
    import urllib.request

    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            x_request_id = response.headers.get("X-Request-Id")
            if x_request_id:
                print(f"X-Request-Id: {x_request_id}")
            else:
                print("No X-Request-Id header found in the response.")
    except urllib.error.URLError as e:
        print(f"Error fetching data from {url}: {e.reason}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
    else:
        fetch_x_request_id(sys.argv[1])
