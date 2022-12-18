# Lista nimistä
names = [
    "Olivia", "Lilja", "Eevi", "Sofia", "Venla", "Aino", "Maria", "Aurora", "Emilia",
    "Leo", "Eino", "Oliver", "Elias", "Väinö", "Olavi", "Juhani", "Johannes", "Mikael"
]

# Käytetään list comprehensonia ja lisätään new_list_of_names -listaan ne nimet, joissa, ei ole
# s- tai e-kirjaimia ja joiden pituus on alle 8 merkkiä
new_list_of_names = [name for name in names if 's' not in name.lower() and 'e' not in name.lower()
                     and len(name) < 8]
names = "\n".join(new_list_of_names)
print(f"Lista nimistä, joissa ei ole s- tai e-kirjaimia ja joiden pituus on alle 8 merkkiä:\n"
      f"{names}")
print()

# Lasketaan nimen vokaalit ja tulostetaan nimet, joissa on enintään 2 vokaalia
# tämäkin olisi kai pitänyt tehdä list comprehensonilla? Mutta aivot eivät nyt taivu siihen
vowel = ['a', 'e', 'i', 'o', 'u', 'y', 'ä', 'ö']
list_of_names = []

for name in new_list_of_names:
    count = 0
    for char in name.lower():
        if char in vowel:
            count = count + 1
    if count < 3:
        list_of_names.append(name)

name = "\n".join(list_of_names)
print(f"Nimet, joissa on lisäksi korkeintaan kaksi vokaalia:\n{name}")