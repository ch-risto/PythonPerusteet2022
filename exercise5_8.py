# Pyydetään käyttäjältä sana ja siirtoluku
word = input("Syötä sana:\n")
count = int(input("Anna siirtoluku:\n"))

# luodaan muuttuja, johon tallennetaan uusi sana
new_word = ""

# käydään sana läpi silmukassa
for n in word:
    # kirjaimen sijainti merkistössä
    index_n = ord(n)
    # merkki annetulla sijoitusluvulla (kirjaimen sijainti + annettu siirtoluku)
    char_n = chr(index_n + count)
    new_word = new_word + char_n

print(new_word)
