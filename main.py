import os
import requests
from dotenv import load_dotenv
from src.database import insert_weather_data

def connect_to_api():
    # API call for Fargo, ND
    try:
        url = f"https://api.openweathermap.org/data/2.5/forecast?lat=46.877186&lon=-96.789803&units=imperial&appid={API_KEY}"
        response = requests.get(url)
        res = response.json()
        print("Success fetching API data for " + res['city']['name'] + "!!!")
        return res
    except Exception as e:
        print(e)

if __name__ == "__main__":
    load_dotenv()
    API_KEY = os.getenv('API_KEY')

    data = connect_to_api()
    insert_weather_data(data)
    print("Data inserted into database successfully!")
