import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import os

load_dotenv(".env")

class DataManager:

    def __init__(self):
        self._authorization = {"Authorization": os.environ["SHEETY_HEADER"]}
        self.destination_data = {}
        self.sheet_endpoint = "https://api.sheety.co/5f01f191335652a1846e49c9d59aee26/flightTracker/sheet1"

    def get_data(self):
        response = requests.get(url=self.sheet_endpoint)
        data = response.json()
        print(data)
        self.destination_data = data["sheet1"]

        return self.destination_data

    def update_codes(self):
        for city in self.destination_data:
            new_data = {
                "sheet1": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{self.sheet_endpoint}/{city['id']}", json=new_data)
            print(response.text)
