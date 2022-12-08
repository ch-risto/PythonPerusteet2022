def show_personal_info(name, city, career):
    print(name)
    print(city)
    print(career)

def count_seconds(hours, minutes, seconds):
    result = hours * 60 * 60 + minutes * 60 + seconds
    return result

def magazine_serial_check(serial):

    issn = False
    # Tarkistetaan syötetyn tekstin pituus ja onko tekstin keskimmäisin (4.) merkki viiva
    if len(serial) == 9 and serial[4] == "-":
        # poistetaan viiva
        serial = serial.replace(serial[4], "")

        # tarkistetaan onko jäljelle jäänyt teksti oikean pituinen ja pelkkiä numeroita
        if serial.isdigit():
            issn = True

    return issn