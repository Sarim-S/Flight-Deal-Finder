import os
from dotenv import load_dotenv
import requests

load_dotenv()

TOKEN_REQUEST_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
TOKEN_HEADER = {
    "Content-Type": "application/x-www-form-urlencoded"
}
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

class FlightSearch:

    def __init__(self):
        self._api_key = os.environ["AITA_KEY"]
        self._api_secret = os.environ["AITA_PASS"]
        self.token = self.get_token()

    def get_token(self):
        TOKEN_BODY = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret,
        }

        response = requests.post(url=TOKEN_REQUEST_ENDPOINT, headers=TOKEN_HEADER, data=TOKEN_BODY)

        return response.json()["access_token"]

    def get_destination_code(self, city_name):

        iataHeader = {
            "Authorization": f"Bearer {self.token}"
        }

        query = {
            "keyword": city_name,
            "max": 2,
            "include": "AIRPORTS"
        }

        response = requests.get(url=IATA_ENDPOINT, headers=iataHeader, params=query)

        print(f"Response code {response.status_code}, data given: {response.text}")

        try:
            code = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"Index: No airport found for {city_name}")
            return "N/A"
        except KeyError:
            print(f"Key: No airport for {city_name}")
            return "N/A"

        return code
