# Luodaan käyttäjälle turvallinen salasana
import random

# Luodaan funktio salasanan luomiseksi
def createPassword(lenght):
    # Luetellaan kaikki merkit, joita salasanassa halutaan käyttää
    base = "abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ1234567890-_~?*$!+%@"
    password = ""

    # arvotaan silmukassa käyttäjän toivoman pituinen salasana
    for n in range(lenght):
        random_index = random.randint(0, len(base))
        character = base[random_index]
        password = password + character

    return password

# tarkistetaan eri funktiossa, jotta voidaan kutsua luomisfunktiota jos salasana ei mene läpi
def passInspection(password):
    validPassword = True
    # Jos salasana sisältää vain kirjaimia tai numeroita:
    if password.isalnum():
        validPassword = False
    # Jos salasana sisältää vain pieniä kirjaimia
    elif password.islower():
        validPassword = False
    # Jos salasana sisältää vain isoja kirjaimia
    elif password.isupper():
        validPassword = False

    return validPassword

# Kysytään käyttäjältä silmukassa kuinka pitkän salasanan hän haluaa (vähintään 8 merkkiä)
again = True
while again:
    lenght = int(input("Kuinka pitkän salasanan haluat luoda? (vähintään 8 merkkiä)\n"))
    if lenght > 7:
        again = False

# Luodaan salasana silmukassa, jossa myös tarkistetaan se. Luodaan uusi salasana niin kauan
# kunnes se läpäisee tarkastuksen
create = True
while create:
    # kutsutaan salasananluomisfunktiota
    password = createPassword(lenght)
    if passInspection(password):
        create = False

# Tulostetaan salasana käyttäjälle
print(f"Turvallinen salasana: {password}")