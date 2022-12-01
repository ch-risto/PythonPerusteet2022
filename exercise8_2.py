# tuodaan tarvittavat moduulit
from colorama import Back, Style
from random import randrange

# Arvotaan random numero väliltä 1-20
number = randrange(1, 20)

# luodaan muuttuja, jolla määritellään ohjelman jatkuvuus
again = True

# luodaan silmukka, jonka sisällä käyttäjää pyydetään arvaamaan numero
while again:
    guess = int(input("Arvaa numero (1-20):\n"))

    # Logiikka, millä tuloksia tulostetaan
    if guess > number:
        print(Back.RED + "Liian korkea" + Style.RESET_ALL)

    if guess < number:
        print(Back.BLUE + "Liian matala" + Style.RESET_ALL)

    if guess == number:
        print(Back.GREEN + "ONNEKSI OLKOON!" + Style.RESET_ALL)
        again = False