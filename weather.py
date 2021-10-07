from datetime import datetime
import requests
import sys

base_weather = []
element = []


class WeatherForecast:

    BASE_URL = 'http://api.weatherapi.com/v1/history.json'

    def __init__(self, api_key, date=str(datetime.today().date())):
        self.api_key = api_key
        self.date = date
        self.data = self.get_data()
        self.base_weather = base_weather
        self.element = element

    def items(self):
        for element in self.base_weather:
            date_element, weather_info = element
            yield (date_element, weather_info)

    def __getitem__(self, item):
        for element in self.base_weather:
            date_element, weather_info = element
            if date == date_element:
                return f'{weather_info}'

    def __iter__(self):
        for element in self.base_weather:
            date_element, weather_info = element
            yield date_element

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
            return "Będzie padać"
        elif totalprecip_mm == 0.0:
            return "Nie będzie padać"
        return "Nie wiem!"



wf = WeatherForecast(api_key=sys.argv[1], date=sys.argv[2])

date = sys.argv[2]


with open(f'weather_history.txt', 'r', encoding='utf8') as file:
    for line in file:
        splitted_line = line.split(';')
        position_1 = splitted_line[0]
        position_2 = splitted_line[1]

        data = [position_1, position_2.replace('\n', '')]

        base_weather.append(data)

tupla = wf.items()
print(tupla)
while True:
    element_list = []
    in_file = False
    print(wf[date])
    in_file = True

    if not in_file:
        print(wf.get_rain_info())
        value = wf.get_rain_info()
        element_list.append(date)
        element_list.append(value)
        base_weather.append(element_list)
    break



with open(f'weather_history.txt', 'w', encoding='utf8') as file:
    for line in base_weather:
        file.write(f'{line[0]}' + ';' + f'{line[1]}' + '\n')

for date in wf:
    print(date)