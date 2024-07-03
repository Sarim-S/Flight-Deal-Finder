from data_manager import DataManager
from flight_data import FlightData

data_manager = DataManager()
sheet_data = data_manager.get_data()

flight_manager = FlightData()
data = flight_manager.get_flight_data(destination_code="PAR")
print(data)

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()

    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n{sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_codes()


