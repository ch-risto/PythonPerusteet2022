import math
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

def show_numbered_list(title, data):
    # tulostetaan otsikko
    print(title)
    data_len = len(data)

    # luodaan silmukka, jossa datan numero ja sisältö tulostetaan
    for n in range(data_len):
        print(f"{n + 1}. {data[n]}")

# luodaan funktiot eri objektien tilavuuden laskemiseksi, kaavat tehtävänannosta
# tuotiin tiedoston alkuun math-kirjasto, jotta voidaan käyttää piitä
def box_volume(width, height, depth):
    return round(width * height * depth, 2)

def ball_volume(radius):
    return round((4 * math.pi * radius ** 3) / 3, 2)

def pipe_volume(radius, length):
    return round(math.pi * radius ** 2 * length, 2)