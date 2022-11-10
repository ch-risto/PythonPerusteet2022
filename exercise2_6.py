# Tuodaan math-kirjasto neliöjuuria ja potensseja varten

import math

# Lasketaan yhden kirsikan arvo

cherry = (2+2*2+2-2-2)/2
#print(f"kirsikka {cherry}")

# Lasketaan eri hedelmien arvot

apple = ((math.sqrt(3+10-4)/3)+(((5**3)-5)/20)+3)
#print(f"apple {apple}")

orange = apple - 9
#print(f"orange {orange}")

banana = (cherry * 2 -10)/3
#print(f"banana {banana}")

pear = banana * 3 -8
#print(f"pear {pear}")

# Lasketaan ja tulostetaan vastaus

print(f"Tulos on: {apple - (banana*2) + (orange*2 * (pear + cherry))}")