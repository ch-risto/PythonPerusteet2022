import json

# luetaan countries.json sitältö muuttujaan ja muutetaan python-dataksi
file_handle = open("countries.json", "r", encoding="utf-8")
content = file_handle.read()
file_handle.close()
countries = json.loads(content)

# tulostetaan silmukassa kaikki maat ja pääkaupungit
print("Kaikki maat ja pääkaupungit:")
for country in countries:
    print(f"{country['country']}: {country['capital']}")

# kysytään käyttäjältä, millä kirjaimella alkavien maiden tiedot halutaan tulostaa
firs_letter = input("Minkä alkukirjaimen maat ja pääkaupungit tulostetaan?\n").upper()

for country in countries:
    if country['country'][0] == firs_letter:
        print(f"{country['country']}: {country['capital']}")