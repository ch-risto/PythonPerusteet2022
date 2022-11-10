# Kysytään opiskelijalta onko hän opiskelija vai ei (k/e)
# pakota capsit pieneen muotoon tms varmista, ettei ohjelman toimiminen jää siitä kiinni
student = input("Oletko opiskelija? (k/e)\n")
student = student.lower()

# Kysy käyttäjältä kuukauden numero ja muutetaan se int
month = int(input("Mille kuukaudelle matka varataan? (1-12)\n"))

# Boolean sille, onko opiskelija oikeutettu alennettuun hintaan
special_price = False

# jos opiskelija
if student == "k":
    special_price = True

    # jos varaus EI OLE kuukausille 6,7 tai 8
    if 6 <= month <= 8:
        special_price = False

# Tulostetaan tieto siitä, myönnetäänkö alennusta
if special_price:
    print("Alennus myönnetty!")
else:
    print("Normaali hinta.")