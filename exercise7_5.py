import json
import urllib.request

url = "https://edu.frostbit.fi/api/weather/"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")

weather = json.loads(raw_data)

strongest_wind = 0
strongest_wind_city = ""
weakest_wind = 0
weakest_wind_city = ""

for city in weather:
    # print(city)
    name = city['location']
    wind = city['wind']
    print(name)
    print(wind)
    print()

    # jos wind on suurempi kuin strongest_wind -> silloin strongest_wind = wind
    # samalla asetetaan talteen mikä oli sekaupunki, missä oli suurin tuuli, eli
    # strongest_wind_city = name jne

    # jos tämän kaupungin tuuli on kovempi kuin strongest_wind
    # -> päivitetään strongest_wind