# Kysytään automatkan pituus
matka = input("Anna matkan pituus:\n")

# Koska tuloksessa tarvitaan desimaaleja, muutetaan muotoon float
matka = float(matka)

# oleletaan että kulutus on 6.5l/100

# Lasketaan kulutus
kulutus = matka/100*6.5

# Määritetään mihin muotoon tulos halutaan
format_kulutus = "{:.1f}".format(kulutus)

print(f"Kulutus: {format_kulutus} l")