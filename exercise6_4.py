# lista tunnisteita
products = ["T1565_2020", "T2432_2019",
            "T8551_2018", "T3345_2019",
            "Y51372_2019", "Y76715_2017",
            "E98144_2018", "T7733_2020",
            "E7614_2021", "E9722_2017",
            "Y82018_2020", "T61287_2021",
            "E9152_2019", "T7749_2021"]

# Pyydetään käyttäjältä vuosiluku
ask = int(input("Minkä vuoden koodit haetaan?\n"))

# luodaan silmukka, jossa käydään listan tuotteet yksi kerrallaan läpi
for p in products:
    # Jaetaan tunnisteet kahteen erilliseen osaan -> tilauskoodi ja vuosiluku
    # muutetaan tekstitunnus listaksi erotusmerkkinä alaviiva
    part = p.split("_")
    order = part[0]
    year = int(part[1])

    # jos vuosi on tilaustunnisteen toisessa osassa, tulostetaan tilauskoodi
    if year == ask:
        print(order)
    # jos ei, jatketaan silmukkaa
    else:
        continue
