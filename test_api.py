import os
import requests

api_key = os.environ.get("the_odds_api_key")
url = "https://api.sportsgameodds.com/v2/sports"
headers = {"x-api-key": api_key}

response = requests.get(url, headers=headers)

print(response.text)
