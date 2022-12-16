# luodaan funktio tiedoston käsittelylle
def read_file(fileName):

    # aukaistaan yhteys tiedostoon read muodossa
    file_handle = open(fileName, "r", encoding="utf-")

    # luetaan koko tiedoston sisältö muuttujaan
    # suljetaan yhteys tiedostoon hyvien tapojen mukaisesti
    return file_handle.read()
    file_handle.close()

content = read_file("artists.txt")

# jaetaan tiedoston sisältö riveihin
lines = content.split("\n")

# Tulostetaan "otsikko" sille mitä tehdään ja for-loopissa
# levyjen tiedot, eli rivit nuolen kanssa
print("Kaikkien aikojen myydyimpiä kotimaisia äänitteitä:")
print()
for n in lines:
    print(f"-> {n}")