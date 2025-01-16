import sys
import requests

# Ensure a URL is provided
if len(sys.argv) == 2:
    url = sys.argv[1]
    print(f"Checking URL: {url}")  # Debugging output to check the URL being processed
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"The website {url} is working.")
        else:
            print(f"The website {url} returned a status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error with the URL {url}: {e}")
else:
    print("Please provide a URL.")
