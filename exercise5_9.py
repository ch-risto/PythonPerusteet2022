names = [
    "Olivia", "Lilja", "Eevi", "Sofia", "Venla", "Aino", "Maria", "Aurora", "Emilia",
    "Leo", "Eino", "Oliver", "Elias", "Väinö", "Olavi", "Juhani", "Johannes", "Mikael", "William"
]

# luodaan boolean, jolla on helpompi seurata täyttääkö nimi ehdot vai ei
passing = False

# Käydään jokainen listan nimi läpi silmukassa
for name in names:
    # muutetaan kaikki nimen kirjaimet pieniksi vertailun helpottamiseksi
    lower_name = name.lower()
    test_name = []
    # Käytetään list comprehensionia jakamaan nimi kirjaimiksi
    name_letters = [letter for letter in lower_name if letter != "s"]
    test_name.append(letter)
    print(name)
    print(test_name)

    if name_letters == name:
        passing = True

    if passing:
        print(name)
    # Rakennetaan ehtolauselogiikka
#    for n in name_letters:
#        if n == "b":
#            passing = False

#        elif n == "e":
#            passing = False

#        if len(name) > 8:
#            passing = False

#    if passing:
        # Tulostetaan ehdot täyttävä nimi
#        print(name)