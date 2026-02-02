import requests
from requests.exceptions import HTTPError


# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200


response2 = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
if response2:
    print(f"Success! Status code: {response2.status_code}")
else:
    raise Exception(f"Non-success status code: {response.status_code}")

URLS = ["https://api.github.com", "https://httpbin.org/status/404", "https://httpbin.org/status/500"]

for url in URLS:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    else:
        print("Success!")

response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "language:python", "sort": "stars", "order": "desc"},
)

json_response = response.json()
popular_repositories = json_response["items"]
for repo in popular_repositories[:3]:
    print(f"Name: {repo['name']}")
    print(f"Description: {repo['description']}")
    print(f"Stars: {repo['stargazers_count']}\n")