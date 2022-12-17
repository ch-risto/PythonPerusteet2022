import json
import datetime

now = datetime.datetime.now()

# aukaistaan yhteys vieraskirjatiedostoon lukumuodossa ja tuodaan data
# dataa tarvitaan sekä luettaessa että kirjoitettaessa vieraskirjaan
# suljetaan yhteys tiedostoon
file_handle = open("guestbook.json", "r", encoding="utf-8")
content = file_handle.read()
file_handle.close()

# tuodaan tiedosto json:ista dictionaryksi
entries = json.loads(content)

# Kysytään käyttäjältä, haluaako hän lukea vai kirjoittaa vieraskirjaa (l/k)
# Tehdään kysymys loopissa, joka kysyy käyttäjältä mitä haluaa tehdä, kunnes vastaa "oikein"
again = True
activity = ""

while again:
    activity = input("Haluatko lukea vai kirjoittaa vieraskirjaa? (l/k)\n")
    if activity == "l" or activity == "k":
        again = False

# Jos lukea, haetaan tiedostosta rivit ja tulostetaan näytölle käyttäen silmukkaa
if activity == "l":

    print("Tervetuloa vieraskirjaan!")
    print()


    # haetaan silmukassa rivejä niin kauan kuin niitä on
    for line in entries:
        print(f"{line['date']}")
        print(f"{line['entry']}")
        print()

# Jos kirjoittaa, tallennetaan rivi tiedoston loppuun
elif activity == "k":
    # Kysytään käyttäjältä mitä haluaa kirjoittaa ja lisätään päivämäärä automaattisesti
    txt = input("Kirjoita uusi viesti:\n")
    day = now.strftime("%d.%m.%y %H:%M")

    # Tallennetaan päivämäärä ja kirjoitettu viesti muuttujaan
    entry = {
        "date": day,
        "entry": txt
    }

    # lisätään uusi kirjoitus kokoelmaan
    entries.append(entry)

    # listasta json-muotoon (tekstiksi)
    guestbook = json.dumps(entries)

    # avataan yhteys tiedostoon, json-tiedostoissa aina kirjoitusmuodossa
    # (erillistä append toimintoa ei tarvita) vaan json kirjoittaa päälle
    file_handle = open("guestbook.json", "w")
    # tallennetaan teksti ja suljetaan yhteys
    file_handle.write(guestbook)
    file_handle.close()

    print("Vieraskirjamerkintäsi on tallennettu")