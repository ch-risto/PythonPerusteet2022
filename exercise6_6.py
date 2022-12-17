basket = ["omena", "banaani", "kirsikka", "porkkana", "peruna", "tomaatti", "kaali"]

# kysytään käyttäjältä jokin sana muuttujaan item
item = input("Syötä sana:\n")

# tarkistetaan onko syötetty sana numero ja onko korissa tarpeeksi tuotteita:
if item.isnumeric() and int(item) <= len(basket):
    item = int(item)-1
    item = basket[item]
    for p in basket:
        if p == item:
            continue
        else:
            print(p)

# tarkistetaan ensin onko sana listassa, jos ei
# tulostetaan käyttäjälle viesti, ettei sanaa löydy listalta
elif item not in basket:
    print("Sanaa ei löytynyt listasta!")

# Muussatapauksessa tulostetaan lista, paitsi kyseistä sanaa
else:
    for p in basket:
        if p == item:
            continue
        else:
            print(p)