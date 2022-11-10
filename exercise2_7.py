# Tuodaan matikkakirjasto

import math

# Kysytään käyttäjältä arvoja

a = input("Syötä ensimmäinen arvo:\n")
a = float(a)

b = input("Syötä toinen arvo:\n")
b = float(b)

c = input("Syötä kolmas arvo:\n")
c= float(c)

# Lasketaan diskriminantti d = b^2-4ac, koska juurten luonne riippuu sen arvosta

D = b ** 2 - 4 * a * c

if D < 0:
    print("Yhtälölle ei ole yhtään reaalilukujuurta.")
    pass

elif D == 0:
   x1 = (-b + (math.sqrt(D))) / (2 * a)
   print(f"Tuloksia on vain yksi: {x1}")
   pass

else:
    x1 = (-b + (math.sqrt(D))) / (2 * a)
    x2 = (-b - (math.sqrt(D))) / (2 * a)
    print(f"Tulos on: {x1} tai {x2}")
    pass
