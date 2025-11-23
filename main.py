import os
import requests
import json

API_KEY = os.environ.get("the_odds_api_key")
print(f"API Key: {API_KEY}")
BASE_URL = "https://api.the-odds-api.com"

def get_nfl_events():
    """Fetches upcoming NFL events and returns their IDs."""
    url = f"{BASE_URL}/v4/sports/americanfootball_nfl/events"
    params = {"apiKey": API_KEY}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        events = response.json()
        return [event["id"] for event in events]
    else:
        print(f"Error fetching events: {response.status_code}")
        print(response.text)
        return []

def main():
    print("Fantasy Forecasting Tool")
    event_ids = get_nfl_events()
    if event_ids:
        print(f"Found {len(event_ids)} upcoming NFL games.")

if __name__ == "__main__":
    main()
