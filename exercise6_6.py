basket = ["omena", "banaani", "kirsikka", "porkkana", "peruna", "tomaatti", "kaali"]

# kysytään käyttäjältä jokin sana muuttujaan item
item = input("Syötä sana:\n")


# tarkistetaan ensin onko sana listassa, jos ei
# tulostetaan käyttäjälle viesti, ettei sanaa löydy listalta
if item not in basket:
    print("Sanaa ei löytynyt listasta!")

# Muussatapauksessa tulostetaan lista, paitsi kyseistä sanaa
else:
    for p in basket:
        if p == item:
            continue
        else:
            print(p)