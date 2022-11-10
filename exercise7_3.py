# luodaan lista
shopcart = [
    {'name': 'Lokki-valaisin', 'price': 349.9},
    {'name': 'Stockholm-matto', 'price': 129.9},
    {'name': 'Malm-lipasto', 'price': 49.9},
    {'name': 'Vienna-divaanisohva', 'price': 799.9},
    {'name': 'Ritz-nojatuoli', 'price': 369.9}
]

# luodaan muuttuja tuotteiden summalle
total = 0

# tulostetaan "otsikko" ennen silmukkaa
print("Kuitti ostoksista:")

# tulostetaan silmukassa jokaisen tuotteen nimi ranskalaisen viivan kanssa
for item in shopcart:
    print("- " + item['name'])

    # lisätään jokaisen tuotteen hinta kokonaissummaan
    total = total + item['price']

print()
# tulostetaan yhteissumma ja toivotetaan tervetuloa uudelleen!
print(f"Yhteensä {total}€.")
print("Tervetuloa uudelleen!")