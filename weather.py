from datetime import datetime
import requests
import sys


class WeatherForecast:

    BASE_URL = 'https://weatherapi-com.p.rapidapi.com/history.json'

    def __init__(self, api_key, date=str(datetime.today().date())):
        self.api_key = api_key
        self.date = date
        self.data = self.get_data()

    def get_data(self):
        request_url = f'{self.BASE_URL}?key={self.api_key}&q=Warsaw&dt={self.date}'
        r = requests.get(request_url)
        content = r.json()
        return content

    def get_temperature(self):
        avg_temp = self.data['forecast']['forecastday'][0]['day']['avgtemp_c']
        return avg_temp

    def get_rain_info(self):
        totalprecip_mm = float(self.data['forecast']['forecastday'][0]['day']['totalprecip_mm'])
        return self.get_rain_chance(totalprecip_mm)