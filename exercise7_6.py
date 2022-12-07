# Kokoelma ravintoloista:
restaurants = {
    0: {
        'name': 'NorthDelish',
         'rating': 4.5,
         'reservations': True,
         'services': [
             'lunch',
             'dinner'],
         'price_level': 5,
         'location': 'Rovaniemi'
    },
    1: {
        'name': 'Food Galore',
         'rating': 3.8,
         'reservations': False,
         'services': [
             'breakfast',
             'lunch'],
         'price_level': 3,
         'location': 'Tornio'
    },
    2: {
        'name': 'Snacksy Oy',
        'rating': 3.2,
        'reservations': False,
        'services': [
            'lunch',
            'dinner',
            ' night'],
        'price_level': 2,
        'location': 'Oulu'
    },
    3: {
        'name': 'NorthDelish',
        'rating': 4.5,
        'reservations': True,
        'services': [
            'lunch',
            'dinner'],
        'price_level': 5,
        'location': 'Rovaniemi'
    },
    4: {
        'name': 'NorthDelish',
        'rating': 4.5,
        'reservations': True,
        'services': [
            'lunch',
            'dinner'],
        'price_level': 5,
        'location': 'Rovaniemi'
    }

}

# luodaan ämpäri ehdotuksille
suggest = []

# Kysellään käyttäjältä kysymyksiä
rate = input("Monenko tähden ravintolan haluat vähintään? (1-5)\n")
price = input("Minkä hintatason ravintolan haluat maksimissaan? (1-5)\n")
reservation = input("Haluatko tehdä etukäteen varauksen? (k/e)\n")
time = input("Mihin kellonaikaan haluat ruokailla? (0-23)\n")

# logiikka kellonaijojen suhteen:
# breakfast = 6-10
# lunch = 11-16
# dinner = 17-24
# night = 0-5

# luodaan silmukka, jossa käydään kaikki ravintolat läpi:
for r in restaurants:
    restaurant = restaurants[r]
    # luodaan silmukka, jossa käydään kaikki ravintolan tiedot läpi
    for n in restaurant:
        value = restaurant[n]
        print(value)

    # luodaan silmukat käyttäjältä kysytyille tiedoille:
    #if 'rating' >= rate:
        #suggest.append(name)

#else:
    #print("Valitettavasti sopivaa ravintolaa ei löytynyt.")

print(suggest)