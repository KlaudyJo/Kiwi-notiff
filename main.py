import pandas as pd
from pretty_html_table import build_table
from datetime import datetime, timedelta
from data import Data
from flight_search import FlightSearch
from emai_sender import EmailSent

data_to_search = Data().
# get destination data from Data() like destination city iata,city name and lowest price 
search_data = data_to_search.get_destination_data()
flight_search = FlightSearch()
# IATA CODE FOR ORIGIN CITY
ORIGIN_CITY = "VIE"
# starting date in week
tomorrow = datetime.now() + timedelta(days=7)
# end date in 2 months
two_months_from_today = datetime.now() + timedelta(days=(2 * 30))
# create empty dataframe
df = pd.DataFrame()
#search for flight based on requirements in data.json and  
destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in search_data}

# Loop through destination dictionorary to found data for each outbound city
for destination_code in destinations:
    flight = flight_search.check_flights(
        ORIGIN_CITY,
        destination_code,
        from_time=tomorrow,
        to_time=two_months_from_today
        
    )
    if flight is None:
        continue
# considering only flight with price below price in data.json
    if flight.price < destinations[destination_code]["price"]:
        # create dictionary from searched data
        result ={'1.outbound_city': flight.outbound_city,
        '2.destination city':flight.destination_city,
        '5.price': flight.price,
        '3.outbound date':flight.outbound_date,
        '4.return date': flight.return_date,
        '6.web link kiwi': flight.link}
        #append to alreday existing dataframe, ignore_index!
        df = df.append(result, ignore_index=True)
# create html table
body = build_table(df, 'blue_light')

# call class EmailSent
sent = EmailSent()
sent.send_email(body, tomorrow, two_months_from_today)
print('email sent')

