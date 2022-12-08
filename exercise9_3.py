from functions import *

# Pyydetään käyttäjää syöttämään ISSN-sarjanumero
serial = input("Anna ISSN-sarjanumero:\n")

# kutsutaan sarjanumeron tarkistusfunktio
result = magazine_serial_check(serial)

if result:
    print("Oikea ISSN")
else:
    print("Väärä ISSN")