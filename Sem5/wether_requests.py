'''
Task 2. https://repl.it/@zhukov/WindingRoughApi#main2.py
'''

import requests as req

def get_wether(city, APIkey):
    r = req.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={APIkey}').json()
    if int(r["cod"]) == 200:
        name = r["name"]
        country = r["sys"]["country"]
        coord = r["coord"]["lon"], r["coord"]["lat"]
        time = int(r["timezone"]) / 3600
        if time > 0:
            timezone = f'UTC+{time}'
        else:
            timezone = f'UTC{time}'
        temp = r["main"]["feels_like"]

        result = {
            'name': f'{name}',
            'country': f'{country}',
            'coord': {
                'lon': f'{coord[0]}',
                'lat': f'{coord[1]}'
            },
            'timezone': f'{timezone}',
            'temp': f'{temp}'
        }
    else:
        result = f'Error: {r["message"]}, {r["cod"]}'
    return result

if __name__ == '__main__':
    cities = ['Chicago, US', 'Saint Petersburg, RU', 'Dhaka, BD']
    APIkey = 'bf3e830b2046f4f7ef63ff2ca100c632'
    for city in cities:
        res = get_wether(city, APIkey)
        print(res)