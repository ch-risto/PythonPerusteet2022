cafe = {
    "name": "Imaginary Cafe Oy",
    "website":  "https://edu.frostbit.fi/sites/cafe",
    "categories": [
        "cafe",
        "tea",
        "lunch",
        "breakfast"
    ],
    "location": {
        "city": "Rovaniemi",
        "address":  "Testikuja 22",
        "zip_code": "96200"
    }
}

# Haetaan dictionaryn sisällä olevista listoista tietoja apumuuttujiin
services = ", ".join(cafe["categories"])
address = cafe["location"]["zip_code"] + " " + cafe["location"]["city"]

# tulostetaan halutut tiedot
print(cafe["name"])
print(cafe["location"]["address"])
print(address)
print()
print(cafe["website"])
print(f"Palvelut: {services}")
