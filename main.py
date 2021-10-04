from datetime import datetime
import requests
import sys

base_weather = []

class WeatherForecast:

    BASE_URL = 'http://api.weatherapi.com/v1/history.json'

    def __init__(self, api_key, date=str(datetime.today().date())):
        self.api_key = api_key
        self.date = date
        self.data = self.get_data()

    def get_data(self):
        request_url = f'{self.BASE_URL}?key={self.api_key}&q=London&dt={self.date}'
        r = requests.get(request_url)
        content = r.json()
        return content

    def get_temperature(self):
        avg_temp = self.data['forecast']['forecastday'][0]['day']['avgtemp_c']
        return avg_temp

    def get_rain_info(self):
        totalprecip_mm = float(self.data['forecast']['forecastday'][0]['day']['totalprecip_mm'])
        return self.get_rain_chance(totalprecip_mm)


    def get_rain_chance(self, totalprecip_mm):
        if totalprecip_mm > 0.0:
            return "Bedzie padac"
        elif totalprecip_mm == 0.0:
            return "Nie bedzie padac"
        return "Nie wiem!"


with open(f'weather_history.txt', 'r') as file:
    for line in file:
        splitted_line = line.split(';')
        position_1 = splitted_line[0]
        position_2 = splitted_line[1]

        data = [position_1, position_2.replace('\n', '')]

        base_weather.append(data)
        print(base_weather)

weather = WeatherForecast(api_key=sys.argv[1], date=sys.argv[2])

date = sys.argv[2]
element = []

while True:
    if date == base_weather[0][0]:
        print(base_weather[0][1])
        break
    else:
        print(weather.get_rain_info())
        value = weather.get_rain_info()
        element.append(date)
        element.append(value)
        base_weather.append(element)
        break
print(base_weather)
with open(f'weather_history.txt', 'a') as file:
    for line in base_weather:
        file.write(f'{line[0]}' + ';' + f'{line[1]}' + '\n')