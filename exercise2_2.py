# Tuodaan math kirjasto, koska tarvitaan mm. neliöjuurta
import math

# Kysytään käyttäjältä muuttujat

a = input("Anna kolmion ensimmäinen kateetti:\n")
a = float(a)

b = input("Anna kolmion toinen kateetti:\n")
b = float(b)

# Kolmion hypotenuusa lasketaan pythagoraan lauseella: a^2 + b^2 = c^2
# Jolloin hypotenuusa c = neliöjuuri(a^2 + b^2)

c = math.sqrt(a**2+b**2)
format_c = "{:.1f}".format(c)

# Tulostetaan vastaus

print(f"Hypotenuusan pituus: {format_c} m")