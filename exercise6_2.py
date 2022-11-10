# Tehdään ohjelma, jolla käyttäjä voi tulostaa haluamansa luvun kertotaulun väliltä 1-10
# ohjelma loppuu ainoastaan silloin, jos käyttäjä syöttää 0:n
# syötetyn luvun tulee olla myös väliltä 1-10, kysytään uutta arvoa niin kauan kuin ehto täyttyy

# luodaan boolean jolla tarkistetaan ohjelman jatkuminen
again = True

# luodaan looppi, joka toimii niin kauan kunnes again = False
while again:

    # pyydetään käyttäjältä luku:
    count = int(input("Minkä luvun kertotaulun haluat nähdä? (1-10). 0 lopettaa ohjelman.\n"))

    # jos käyttäjän syöttämä luku on 0, lopetetaan ohjelma
    if count == 0:
        again = False

    # jos käyttäjän syöttämä luku ei ole välillä 1-10, tulostetaan "virheviesti"
    elif count > 10 or count < 0 :
        print("Vääränlainen luku.")
        print()

    # muussa tapauksessa tulostetaan luvulle kertotaulu 1-10, lisätään x:n 1, jotta aloitetaan 1:stä
    else:
        for x in range(10):
            print(f"{count} x {x+1} = {count * (x+1)}")
        print()