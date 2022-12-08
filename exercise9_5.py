from functions import *

# tehdään boolean, jolla määritellään ohjelman kesto
again = True

while again:

    # Kysytään käyttäjältä mitä haluaa tehdä:
    fun = input("Valitse toimenpide (1-3), 0 lopettaa ohjelman:\n"
                "1 = laatikko, 2 = pallo, 3 = putki\n")

    # Määritellään mitä tapahtuu jos käyttäjä syöttää 0
    if fun == "0":
        print("Kiitos ohjelman käytöstä!")
        again = False

    # Muissa tapauksissa kysytään käyttäjältä funktion ajamiseen tarvittavat tiedot
    # sekä tulostetaan funktion laskema tulos
    elif fun == "1":
        width = int(input("Anna laatikon leveys:\n"))
        height = int(input("Anna laatikon korkeus:\n"))
        depth = int(input("Anna laatikon syvyys:\n"))
        print(f"Laatikon tilavuus: {box_volume(width, height, depth)} m3")
        print()

    elif fun == "2":
        radius = int(input("Anna pallon säde:\n"))
        print(f"Pallon tilavuus: {ball_volume(radius)} m3")
        print()

    elif fun == "3":
        radius = int(input("Anna putken säde:\n"))
        length = int(input("Anna putken pituus:\n"))
        print(f"Putken tilavuus: {pipe_volume(radius, length)} m3")
        print()