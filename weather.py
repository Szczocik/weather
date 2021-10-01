from datetime import datetime
import requests
import sys


class WeatherForecast:

    BASE_URL = 'https://weatherapi-com.p.rapidapi.com/history.json'

    def __init__(self, api_key, date=str(datetime.today().date())):
        self.api_key = api_key
        self.date = date
        self.data = self.get_data()
