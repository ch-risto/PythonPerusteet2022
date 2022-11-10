# Karkausvuosi on jaollinen 4:llä, muttei sadalla.
# Vuosi, joka on jaollinen 400:lla, on karkausvuosi.

# Pyydetään käyttäjää syöttämään vuosiluku

year = input("Anna vuosiluku:\n")
year = int(year)

if year % 400 == 0 :
    print("Karkausvuosi.")
elif year % 100 == 0 :
    print("Ei ole karkausvuosi.")
elif year % 4 == 0 :
    print("Karkausvuosi.")
else:
    print("Ei ole karkausvuosi.")