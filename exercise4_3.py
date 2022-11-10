# annettu teksti:
text = "The quick brown fox jumps over the lazy dog. That \
sentence contains every letter in the English alphabet. Neat!"

print(text)
# a) Muokkaa text-muuttujaa niin, että "fox" vaihdetaan sanaan "duck"
print("")

text = text.replace("fox", "duck")
print(text)

# b) pyydä käyttäjältä jokin sana, joka poistetaan text-muuttujasta
#   Jos sanaa ei löydy, tulosta "Sanaa ei löytynyt"
#   Jos poistettava sana löytyi, poista sana muuttujasta ja tulosta teksti uudelleen näytölle
print("")

word = input("Anna poistettava sana:\n")

if word not in text:
    print("Sanaa ei löytynyt!")
else:
    text = text.replace(word+" ", "")
    print(text)

# c) tulosta text-muuttujassa olevien merkkien lukumäärä
#   Lisätehtävä: tulosta myös sanojen lukumäärä
print("")

print(f"Muuttujassa on {len(text)} merkkiä ja {len(text.split())} sanaa.")

# d) Muuta text-muuttujan tekstin pisteet rivinvaihdoiksi. Tulosta teksti näytölle
print("")

print(text.replace(". ", "\n"))

# e) Pyydä käyttäjältä jokin lause, tallenna se input() avulla muuttujaan nimeltä usertext
#   tee if-lause, ja jos usertext on 20 tai alle merkkiä pitkä, tulosta teksti sellaisenaan
#   jos usertext onkin yli 20 merkkiä pitkä, lyhennä se tasan 20 merkkiin ja lisää perään ...
#    tulosta lyhennetty versio tämän jälkeen
print("")

usertext = input("Anna jokin lause:\n")

if len(usertext) < 20:
    print(usertext)
else:
    print(usertext[0:20] + "...")