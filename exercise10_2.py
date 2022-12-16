import datetime

now = datetime.datetime.now()

# Vieraskirjaohjelma
# Ihan ensimmäiseksi luodaan tiedosto. x:llä tiedoston luominen ja tiedostoon kirjoittaminen
# luo virheen jos tiedosto on jo olemassa, eli kommentoidaan pois ekan kutsun jälkeen
#file_create = open("guestbook.txt", "x")
#file_create.write("Tervetuloa käyttämään vieraskirjaa!\n")
#file_create.close()

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

    # aukaistaan yhteys tiedostoon lukumuodossa ja tuodaan data luettavaksi
    file_handle = open("guestbook.txt", "r")

    # haetaan silmukassa rivejä niin kauan kuin niitä on
    while True:
        line = file_handle.readline()
        print(line)

        if not line:
            break

# Jos kirjoittaa, tallennetaan rivi tiedoston loppuun
elif activity == "k":
    txt = input("Kirjoita uusi viesti:\n")

    file_handle = open("guestbook.txt", "a")
    file_handle.write(f"{now.day}.{now.month}.{now.year} {now.hour}:{now.minute} {txt}\n")

# hyvien tapojen mukaisesti myös suljetaan yhteys tiedostoon
file_handle.close()