# Luodaan tehtävässä vaadittu lista
cities = ["Rooma", "Ateena", "Tukholma", "Lontoo", "Dublin", "Pariisi"]

# kuinka monta elementtiä on listassa
amount = len(cities)

# järjestetään kaupungit aakkosjärjestykseen. perus-sort: cities.sort()
# kun halutaan varmistaa, ettei isoilla ja pienillä alkukirjaimilla ole väliä:
cities.sort(key=lambda v: v.upper())

# haetaan järjestysnumerot ja kaupungit yksi kerrallaan elementtien kokonaismäärästä
for index in range(amount):
    city = cities[index]
# Tulostetaan jokaisen elementin numero alkaen 1. sekä kaupunki
    print(f"{index +1}: {city}")