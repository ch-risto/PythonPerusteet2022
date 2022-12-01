# Tuodaan tarvittavia kirjastoja
import json
import urllib.request

# Haetaan säätiedot netistä
url = "https://edu.frostbit.fi/api/weather/"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")

# Tallennetaan data weather-muuttujaan
weather = json.loads(raw_data)

# Luodaan muuttujat kovimmalle ja heikoimmalle tuulelle
# ja niiden kaupungeille sekä eri alueiden tuulen nopeuksille
strongest_wind = 0
strongest_wind_city = ""
weakest_wind = 0
weakest_wind_city = ""
wind_lapland = []
wind_middle = []
wind_south = []

# Käydään läpi tiedot weather muuttujasta
for city in weather:

    # Luodaan muuttujat tutkittaville tiedoille
    # tarkastelun helpottamiseksi
    name = city['location']
    wind = city['wind']

    # luodaan ehtolause, jossa tallennetaan heikoin tuuli
    if wind < weakest_wind or weakest_wind == 0:
        weakest_wind = wind
        weakest_wind_city = name

    # luodaan samanlainen ehtolause kovimmalle tuulelle
    if wind > strongest_wind or strongest_wind == 0:
        strongest_wind = wind
        strongest_wind_city = name

    # luodaan "ämpärit" eri alueiden tuulen nopeuksille keskiarvon laskemiseksi
    if city['area'] == 'lapland':
        wind_lapland.append(city['wind'])

    if city['area'] == 'middle':
        wind_middle.append(wind)

    if city['area'] == 'south':
        wind_south.append(wind)

# lasketaan alueelliset keskiarvot
average_lapland = round(sum(wind_lapland)/len(wind_lapland), 2)
average_middle = round(sum(wind_middle)/len(wind_middle), 2)
average_south = round(sum(wind_south)/len(wind_south), 2)

# Tulostetaan vertailun tulos
print(f"Tänään eniten tuulee sijainnissa: {strongest_wind_city}, {strongest_wind} m/s")
print(f"Tänään vähiten tuulee sijainnissa: {weakest_wind_city}, {weakest_wind} m/s")
print()

# Tulostetaan tuulennopeuksien keskiarvot
print(f"Keskimääräinen tuuli, Lappi: {average_lapland} m/s")
print(f"Keskimääräinen tuuli, Maan keskiosa: {average_middle} m/s")
print(f"Keskimääräinen tuuli, Etelä-Suomi: {average_south} m/s")