import requests
import datetime
from flight_search import FlightSearch

FLIGHT_ENDPOINT = "test.api.amadeus.com/v2/shopping/flight-offers"

flight_search = FlightSearch()
token = flight_search.token

departure_day = datetime.date.today() + datetime.timedelta(days=1)
year = departure_day.strftime(format="%Y")
month = departure_day.strftime(format="%m")
day = departure_day.strftime(format="%d")

DEPARTURE = f"{year}-{month}-{day}"


class FlightData:

    def __init__(self):
        pass

    def get_flight_data(self, destination_code):

        flight_headers = {
            "Authorization": f"Bearer: {token}"
        }

        flight_parameters = {
            "originLocationCode": "DEN",
            "destinationLocationCode": destination_code,
            "departureDate": DEPARTURE,
            "adults": 1,
        }

        response = requests.get(url=FLIGHT_ENDPOINT, headers=flight_headers, params=flight_parameters)
        data = response.json()
        return data