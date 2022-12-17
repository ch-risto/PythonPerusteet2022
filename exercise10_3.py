import random

# luodaan lista-muuttuja, johon luetaan tekstitiedoston mietelauseet
words_of_wisdom = []

# luetaan tiedosto muuttujaan
file_handle = open("wisewords.txt", "r", encoding="utf-8")

# luetaan tiedoston sisältö listaksi
while True:
    line = file_handle.readline()
    words_of_wisdom.append(line)

    if not line:
        break
        file_handle.close()

# arvotaan random numero listan pituuden perusteella
max_index = len(words_of_wisdom) -1
todays_word = random.randint(0, max_index)

# Tulostetaan päivän mietelause:
print("Päivän mietelause:")
print(words_of_wisdom[todays_word])