# luodaan muuttuja, jolla lasketaan kierrosten määriä
x = 0

# luodaan muuttuja, joka pitää yllä tämän hetken isointa numeroa
biggest = 0

# luodaan silmukka 5:n positiivisen luvun kysymiseen
for x in range(5):
    x = x + 1

    # kysytään käyttäjältä lukua:
    count = int(input("Anna numero:\n"))

    # jos käyttäjän syöttämä luku on suurempi, kuin tämän hetken suurin numero,
    # korvataan se uudella, muussa tapauksessa ohjelma jatkaa muutoksitta
    if count > biggest:
        biggest = count
    else:
        continue

print(f"Suurin käyttäjän luku: {biggest}")