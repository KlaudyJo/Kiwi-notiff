import requests
from flightData import FlightOutputData
#TEQUILA API KIWI.COM
ENDPOINT = [ENDPOINT]
# api key obtained from kiwi.tequila.com after registration for non-commercial use
API_KEY = [API KEY]

# class defines method for flightsearch
class FlightSearch:
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        apikey = {"apikey": API_KEY}
        params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 1,
            "nights_in_dst_to": 5,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }
        response = requests.get(url=f"{ENDPOINT}/v2/search",headers=apikey,params=params,)

        try:
            # parse json response
            data = response.json()["data"][0]
            #print(data)
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightOutputData(
            price=data["price"],
            outbound_city=data["route"][0]["cityFrom"],        
            destination_city=data["route"][0]["cityTo"],
            outbound_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
            link=data["deep_link"]
        )
        return flight_data
