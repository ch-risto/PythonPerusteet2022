# Tuodaan ohjelmaan random kirjasto

import random

# Arvo luku 1 ja 10 väliltä

num1 = random.randint(1, 10)

# Tulostetaan luku

print(f"Arvottu luku: {num1}")

# Arvo ja tulosta suorakulmion kahden sivun pituudet väliltä 2 ja 10

a = random.randint(2, 10)
print(f"Arvottu 1. sivu: {a}")

b = random.randint(2, 10)
print(f"Arvottu 2. sivu: {b}")

# Laske ja tulosta suorakulmion pinta-ala

print(f"Arvotuista sivuista laskettu pinta-ala: {a*b}")