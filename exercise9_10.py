import random
from random import randint
# luodaan lambda, joka palauttaa booleanin riippuen siitä onko annettu kokonaisluku
# parillinen vai pariton. Koska tehtävänannossa pyydetäänkin palauttamaan parittomat
# luvut, tehdäänkin funktio myös niiden filtteröimiselle (varmaan jollain olisi saanut käytettyä
# myös parillisten lambdaa, mutta näin oli nyt nopeampi ja helpompi)
even = lambda a : a % 2 == 0
odd = lambda a : a % 2 != 0

# luodaan kokoelma, jossa on satunnaisesti parillisia ja parittomia lukuja
# Käytetään randomia, koska ei jakseta näpytellä itse, kopioidaan ja liitetään tulostettu lista
# random_index = [random.randint(1, 100) for x in range(25)]
random_index = [60, 12, 98, 3, 27, 93, 64, 61, 31, 32, 16, 2, 51,
                83, 81, 49, 76, 72, 41, 36, 48, 6, 29, 14, 7]

# filtteröidään kokoelmasta parittomat luvut käyttämättä aiemmin tehtyä lambdaa
even_numbers = filter(even, random_index)
print("Parillisia lukuja ovat:")
even_numbers = ", ".join(map(str, list(even_numbers)))
print(even_numbers)
print()

# Filtteröidään ja tulostetaan parittomat numerot
odd_numbers = filter(odd, random_index)
print("Parittomia lukuja ovat:")
print(", ".join(map(str, list(odd_numbers))))
print()

# Tehdään map-funktiolla lista booleaneista ja tulostetaan se
mapped_numbers = map(even, random_index)
print("Lista kokoelman boodeaneista (onko parillinen vai ei):")
print(", ".join(map(str, list(mapped_numbers))))