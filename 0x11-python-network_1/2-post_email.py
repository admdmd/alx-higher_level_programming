#!/usr/bin/python3
"""
This script takes a URL and an email;
-sends a POST request to the URL with the email as a parameter,
-displays the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: ./post_email.py <URL> <email>")

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    try:
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.URLError as e:
        print("Error:", e.reason)
        sys.exit(1)
