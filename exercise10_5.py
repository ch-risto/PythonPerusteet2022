# Huoltokirjausohjelma
import json
import datetime
import os.path

now = datetime.datetime.now()
date = now.strftime("%d.%m.%y")
entries = []

# jos huoltokirjatiedosto on jo olemassa
if os.path.isfile("maintenance.json"):
    # Aukaistaan huoltokirjausohjelma ja tuodaan json-data muuttujaan, josta dictionaryksi
    file_handle = open("maintenance.json", "r", encoding="utf-8")
    content = file_handle.read()
    entries = json.loads(content)
    file_handle.close()

    # tulostetaan viimeisin kirjaus
    print("Viimeisin kirjaus..")
    print(f"Pvm: {entries[-1]['date']}")
    print(f"Hlö: {entries[-1]['name']}")
    print(f"Tilannekoodi: {entries[-1]['occasion']}")
    print(f"Viesti: {entries[-1]['message']}")
    print()

# Kysytään käyttäjältä kirjattavia tietoja
print("Tee uusi kirjaus:")
name = input("Hlö: ")
occasion = input("Tilannekoodi: ")
message = input("Viesti: ")

# Tallennetaan kysytyt tiedot ja päivämäärä listaan:
entry = {
    "date": date,
    "name": name,
    "occasion": occasion,
    "message": message
}

# Lisätään uusi lista dictionaryn jatkoksi ja muutetaan json-muotoon
entries.append(entry)
maintenance = json.dumps(entries)

# avataan tiedosto kirjoitusmuodossa ja tallennetaan uusi lista
file_handle = open("maintenance.json", "w")
file_handle.write(maintenance)
file_handle.close()
print("Kirjauksesi on tallennettu!")