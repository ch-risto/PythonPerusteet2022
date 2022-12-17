import datetime

thisyear = int(datetime.datetime.now().year)

# Kysytään käyttäjältä tietoja silmukassa.
ask_about_car = True
while ask_about_car:
    original_price = int(input("Mikä on auton alkuperäinen hinta?\n"))
    year = int(input("Mikä on auton valmistusvuosi?\n"))
    km = int(input("Kuinka monta kilometria autolla on ajettu?\n"))
    category = input("Auton valmistajan hintakategoria? (1 tai 2)\n")
    imported_car = input("Onko kyseessä tuontiauto? (k/e)\n").lower()

    # luodaan muuttujia ja määritellään laskemiseen tarvittavia arvoja
    price = original_price
    car_age = thisyear - year
    km_per_year = km / car_age

    if category == "1":
        if km_per_year < 3000:
            # auton arvo laskee 5% jokaista vuotta kohden ensimmäisen viiden ikävuodej aikana
            # sen jälkeen 3% jokaista vuotta kohden
            # lasketaan hintaa silmukassa sen perusteella kuinka vanha auto on
            # Varmistetaan lisäksi, ettei hinta koskaan laske alle 18% alkuperäisestä hinnasta
            if car_age <= 5:
                for n in range(car_age):
                    price = price * 0.95
                    if price <= original_price * 0.18:
                        break
                else:
                    price = price * 0.95 ** 5
                    for n in range(car_age - 5):
                        price = price * 0.95
                        if price <= original_price * 0.18:
                            break

        else:
            # auton arvo laskee 7%/per vuosi ensimmäisen viiden vuoden ajan
            # ja 4% jokaista seuraavaa vuotta kohden
            if car_age <= 5:
                for n in range(car_age):
                    price = price * 0.93
                    if price <= original_price * 0.18:
                        break
            else:
                price = price * 0.93 ** 5
                for n in range(car_age - 5):
                    price = price * 0.96
                    if price <= original_price * 0.18:
                        break



    elif category == "2":
        if km_per_year < 3000:
            # auton arvo laskee 8% jokaista vuotta kohden ensimmäisen viiden ikävuodej aikana
            # sen jälkeen 5% jokaista vuotta kohden
            # lasketaan hintaa silmukassa sen perusteella kuinka vanha auto on
            # Varmistetaan lisäksi, ettei hinta koskaan laske alle 12% alkuperäisestä hinnasta
            if car_age <= 5:
                for n in range(car_age):
                    price = price * 0.92
                    if price <= original_price * 0.12:
                        break
                else:
                    price = price * 0.92 ** 5
                    for n in range(car_age - 5):
                        price = price * 0.95
                        if price <= original_price * 0.12:
                            break

        else:
            # auton arvo laskee 10%/per vuosi ensimmäisen viiden vuoden ajan
            # ja 7% jokaista seuraavaa vuotta kohden
            if car_age <= 5:
                for n in range(car_age):
                    price = price * 0.9
                    if price <= original_price * 0.12:
                        break
            else:
                price = price * 0.9 ** 5
                for n in range(car_age - 5):
                    price = price * 0.93
                    if price <= original_price * 0.12:
                        break

    else:
        again = input("Jotain meni pieleen, kokeillaanko uudelleen?")
        if again == "e":
            ask_about_car = False

    if imported_car == "k":
        price = price * 1.24

    print(f"Käytetyn auton myyntihinta on: {round(price, 2)}€")

    again = input("Haluatko syöttää uuden auton tiedot ohjelmaan? (k/e)\n").lower()
    if again == "e":
        ask_about_car = False
        print("Kiitos ohjelman käytöstä!")